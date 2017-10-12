import nltk, random


class GenderApp(object):
    def __init__(self):
        names_sample = nltk.corpus.names
        self.names = [(name.lower(), 'male') for name in names_sample.words('male.txt')] + [(name.lower(), 'female')
                                                                         for name in names_sample.words('female.txt')]
        random.shuffle(self.names)
        self.feature_sets = [(GenderApp.gender_features_part2(name), gender) for name, gender in self.names]
        self.train_set = self.feature_sets[:2000]
        self.test_set = self.feature_sets[2000:]
        self.classifier = nltk.NaiveBayesClassifier.train(self.train_set)

    @staticmethod
    def gender_features_part2(word):
        name = word.lower()  # let's normalise our input
        features = dict()
        features['first_letter'] = name[0]
        features['last_letter'] = name[-1:]
        features['second_letter'] = name[1]
        features['last_2_letters'] = name[-2:]
        features['first_2_letters'] = name[0:2]
        features['Length'] = len(name)
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            features['' + letter] = name.count(letter)
            features['has' + letter] = letter in name
        return features

    def check_gender(self, name):
        name = name.lower()
        print('Gender for ' + name + ' : ' + self.classifier.classify(GenderApp.gender_features_part2(name)))

    def check_accuracy_of_the_classifier(self):
        print('Accuracy of classifier is : ', nltk.classify.accuracy(self.classifier, self.test_set) * 100)

    def see_learned_information_of_classifier(self, n=10):
       self.classifier.show_most_informative_features(n)

if __name__ == '__main__':
    app = GenderApp()
    app.check_gender('rupal')
    app.see_learned_information_of_classifier(20)
    app.check_accuracy_of_the_classifier()
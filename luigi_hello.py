import luigi

class Hello_luigi(luigi.Task):
    def requires(self):
        pass

    def output(self):
        return luigi.LocalTarget('./output/hello.txt')


    def run(self):
        with self.output().open('w') as f:
            f.write('hello World')



class BaseSentense(luigi.Task):
    params = luigi.Parameter()

    def requires(self):
        pass


    def output(self):
        return luigi.LocalTarget('./ouput/params.txt')


    def run(self):
        with self.output().open('w') as f:
            f.write(self.params)

    



class Addok(luigi.Task):
    params = luigi.Parameter()

    def requires(self):
        return BaseSentense(params = self.params)

    def output(self):
        return luigi.LocalTarget('./output/params-ok.txt')

    def run(self):
        with self.input().open('r') as f:
            input_string = next(f)
        
        with self.output().open('w') as f:
            f.write(f'{input_string}--ok')

if __name__ == '__main__':
    luigi.run()
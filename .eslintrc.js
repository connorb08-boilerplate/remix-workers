/** @type {import('eslint').Linter.Config} */
module.exports = {
    extends: [
        '@remix-run/eslint-config',
        '@remix-run/eslint-config/node',
        'airbnb',
        'airbnb-typescript',
        'prettier',
    ],
    parserOptions: {
        project: './tsconfig.json',
    },
    plugins: ['prettier'],
    ignorePatterns: ['*.js', 'server.ts'],
    rules: {
        'prettier/prettier': ['error'],
        'react/react-in-jsx-scope': 'off',
        'react/jsx-uses-react': 'off',
        'no-unused-vars': 'off',
        '@typescript-eslint/no-unused-vars': [
            'warn', // or "error"
            {
                argsIgnorePattern: '^_',
                varsIgnorePattern: '^_',
                caughtErrorsIgnorePattern: '^_',
            },
        ],
    },
};

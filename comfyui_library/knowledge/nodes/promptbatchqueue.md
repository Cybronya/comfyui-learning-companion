# PromptBatchQueue

## 节点类型

`PromptBatchQueue`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `提示词文本:STRING`（2 次）
- `分割方式:COMBO`（2 次）
- `自定义分隔符:STRING`（2 次）
- `跳过空白:BOOLEAN`（2 次）
- `去除首尾空格:BOOLEAN`（2 次）
- `随机顺序:BOOLEAN`（2 次）
- `随机种子:INT`（2 次）
- `添加前缀:STRING`（2 次）
- `添加后缀:STRING`（2 次）
- `最少字符数:INT`（2 次）

## 输出

- `提示词:STRING`（2 次）
- `队列信息:STRING`（2 次）
- `总数量:FLOAT,INT,NUMBER,STRING`（1 次）
- `总数量:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "按行分割", "---", true, true, false, 819120590388574, "randomize", "", "", 0]`（1 次）
- `["", "按行分割", "---", true, true, false, 317452574130426, "randomize", "", "", 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

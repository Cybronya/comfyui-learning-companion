# ImpactStringSelector

## 节点类型

`ImpactStringSelector`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `strings:STRING`（6 次）
- `multiline:BOOLEAN`（6 次）
- `select:INT`（6 次）

## 输出

- `STRING:STRING`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["0.反推我提供的参考图，按 SYSTEM 内部清单逐项还原，把内容直接融成一段中文提示词输出（不要单独列出画面分析）。每个可见元素都要具体到可执行的视觉细节，禁止概括省略——细节逐件写明材质颜色位置造型，材质逐层逐部件写明表面处理与纹理`（6 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

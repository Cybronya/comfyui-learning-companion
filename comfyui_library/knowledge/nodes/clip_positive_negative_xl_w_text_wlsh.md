# CLIP Positive-Negative XL w/Text (WLSH)

## 节点类型

`CLIP Positive-Negative XL w/Text (WLSH)`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `clip:CLIP`（1 次）

## 输出

- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `positive_text:STRING`（1 次）
- `negative_text:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1024, 1024, 0, 0, 1024, 1024, "niji,Nijistyle,1 girl,close-up,bare shoulder,sexy,cleavage,portrait,neon hair,curly hair`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

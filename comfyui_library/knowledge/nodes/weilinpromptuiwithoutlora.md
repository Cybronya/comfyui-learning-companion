# WeiLinPromptUIWithoutLora

## 节点类型

`WeiLinPromptUIWithoutLora`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `opt_text:*`（1 次）
- `opt_clip:CLIP`（1 次）
- `positive:STRING`（1 次）
- `auto_random:BOOLEAN`（1 次）
- `temp_str:STRING`（1 次）
- `random_template:STRING`（1 次）

## 输出

- `STRING:STRING`（1 次）
- `CONDITIONING:CONDITIONING`（1 次）
- `CLIP:CLIP`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["一张实验性编辑海报, 以参考图片作为主要构图、视觉节奏、拼贴层次、图形密度和配色方式的依据.主体角色使用初音未来, 保留她具有辨识度的经典动漫角色身份与整体轮廓, 也不要添加与角色无关的额外特征.将初音未来放置在画面中央的纵向主体区域,`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

# SDXLPromptStyler

## 节点类型

`SDXLPromptStyler`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输出

- `text_positive:STRING`（2 次）
- `text_negative:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["full body,(Empty Background:1.5\n）,chibi:2,Flat:1.5,(full body:2）,Simple details，", "Realism, photo-realism, real mate`（1 次）
- `["impressionism，monet，  oil painting, ，outdoors, sky, day, cloud, ,Donkey, no_humans, animal, scenery, animal_focus, fie`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

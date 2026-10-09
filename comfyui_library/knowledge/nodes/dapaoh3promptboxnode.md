# DapaoH3PromptBoxNode

## 节点类型

`DapaoH3PromptBoxNode`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `📝 H3提示词:STRING`（1 次）
- `🧩 H3素材清单:STRING`（1 次）

## 输出

- `📝 H3提示词:STRING`（1 次）
- `🧩 H3素材标记:DAPAO_H3_REFERENCES`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["\n\n\n生成依次以 \n\n\n<Picture 1>\n\n\n、\n \n\n\n<Picture 2>和<Picture 3>\n还有\n<Picture 4> 的每个人物各自单独镜头一个人单独的阴湿风格视频，让人物头发和面容`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

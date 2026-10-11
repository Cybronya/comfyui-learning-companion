# DirectorSceneIterator

## 节点类型

`DirectorSceneIterator`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `scene_index:INT`（3 次）
- `role_list:STRING`（3 次）
- `instruct_list:STRING`（3 次）
- `text_list:STRING`（3 次）
- `visual_prompts:STRING`（3 次）
- `video_prompts:STRING`（3 次）
- `char_img1_list:IMAGE`（3 次）
- `char_img2_list:IMAGE`（3 次）
- `char_img3_list:IMAGE`（3 次）
- `char_img4_list:IMAGE`（3 次）

## 输出

- `当前Role:STRING`（3 次）
- `Instruct(含Role):STRING`（3 次）
- `Text(含Role):STRING`（3 次）
- `当前画面Prompt:STRING`（3 次）
- `当前视频运镜(Single):STRING`（3 次）
- `Img1:IMAGE`（3 次）
- `Img2:IMAGE`（3 次）
- `Img3:IMAGE`（3 次）
- `Img4:IMAGE`（3 次）
- `Img5:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

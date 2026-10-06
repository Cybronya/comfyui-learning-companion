# QwenPERewriteT8

## 节点类型

`QwenPERewriteT8`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 42 个 workflow 中。

## 输入

- `image_1:IMAGE`（48 次）
- `image_2:IMAGE`（48 次）
- `image_3:IMAGE`（48 次）
- `image_4:IMAGE`（48 次）
- `image_5:IMAGE`（48 次）
- `image_6:IMAGE`（48 次）
- `image_7:IMAGE`（48 次）
- `image_8:IMAGE`（48 次）
- `image_9:IMAGE`（48 次）
- `image_10:IMAGE`（48 次）

## 输出

- `rewritten_prompt:STRING`（48 次）
- `pe_result:PE_RESULT`（48 次）
- `diagnostics:STRING`（48 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "edit", "auto", "auto", false, "pe_t2i_heretic-Q4_K_M.gguf", "Qwen-Image-2.1-PE-I2I.Q4_K_M.gguf", "Qwen-Image-2.1-P`（8 次）
- `["Create a photorealistic high-definition vertical 9:16 ancient-style portrait with the theme of serving tea in a stone `（6 次）
- `["", "edit", "auto", "auto", false, "pe_t2i_heretic-Q4_K_M.gguf", "pe_i2i_heretic-Q4_K_M.gguf", "Auto", "after_run", 103`（6 次）
- `["一个姑娘", "auto", "auto", "auto", false, "pe_t2i_heretic-Q4_K_M.gguf", "pe_i2i_heretic-Q4_K_M.gguf", "Auto", "after_run",`（5 次）
- `["对这张目标图片进行完整深度解析，按照主体内容（性别、肤色、头发、脸型、服装、配饰等一切信息）、主体姿态、光照和光源信息、相机构图信息、艺术质量（艺术风格：CG、写实、摄影、二次元、赛璐璐等）、构图信息、图片景深信息等7个维度逐一项精细化`（5 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

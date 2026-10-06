# llama_cpp_instruct_adv

## 节点类型

`llama_cpp_instruct_adv`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 35 个 workflow 中。

## 输入

- `llama_model:LLAMACPPMODEL`（42 次）
- `parameters:LLAMACPPARAMS`（42 次）
- `images:IMAGE`（42 次）
- `queue_handler:*`（42 次）
- `preset_prompt:COMBO`（42 次）
- `custom_prompt:STRING`（42 次）
- `system_prompt:STRING`（42 次）
- `inference_mode:COMBO`（42 次）
- `max_frames:INT`（42 次）
- `max_size:INT`（42 次）

## 输出

- `output:STRING`（42 次）
- `output_list:STRING`（42 次）
- `state_uid:INT`（42 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Empty - Nothing", "在男人所穿的白色T恤正面胸口位置，印上黑色文字【Ccm我爱你】，横向居中，宽度约占T恤正面三分之一", "你是MiniMax H3图像编辑工作流的提示词工程师，你能看到当前图片。把用户的修改意图改写`（5 次）
- `["Empty - Nothing", "反推我提供的参考图，按 SYSTEM 内部清单逐项还原，把内容直接融成一段中文提示词输出（不要单独列出画面分析）。严格守格式铁锁。在忠实还原的基础上，为主体和场景叠加电影感视觉渲染（如 85mm 人`（4 次）
- `["Prompt Style - Extreme Detailed", "对这张目标图片进行完整深度解析，按照主体内容（性别、肤色、头发、脸型、服装、配饰等一切信息）、主体姿态、光照和光源信息、相机构图信息、艺术质量（艺术风格：CG、写实、`（3 次）
- `["Prompt Style - Extreme Detailed", "", "", "one by one", 24, 256, 865287117399288, "randomize", true, false]`（3 次）
- `["Empty - Nothing", "反推我提供的参考图，按 SYSTEM 内部清单逐项还原，把内容直接融成一段中文提示词输出（不要单独列出画面分析）。严格守格式铁锁。在忠实还原的基础上，为主体和场景叠加电影感视觉渲染（如 85mm 人`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)

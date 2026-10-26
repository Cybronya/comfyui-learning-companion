---
name: image_to_image_lora_sampler_clip_4
type: Image To Image
frequency: 23
level: weak
coverage: 0.926
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/东方阳台美女Qwen2512真实人像质感御姐美女_2040720553853591554.json, 图片生成/图生图/中文文字重绘-QWen-Image-Instantx-Controlnet_1966363579702259713.json, 图片生成/图生图/人物换背景-QWen-Image-Instantx-Controlnet_1966295550452822018.json, 图片生成/图生图/俯视户外Qwen2512真实人像质感御姐美女_2040701228971200514.json, 图片生成/图生图/古风美女Qwen2512真实人像质感御姐美女_2040756043898163202.json, 图片生成/图生图/吊带睡衣Qwen2512真实人像质感御姐美女_2040694310089265154.json, 图片生成/图生图/城市夜景Qwen2512真实人像质感御姐美女_2040747964653641729.json, 图片生成/图生图/婚纱美女Qwen2512真实人像质感御姐美女_2040750860522758145.json, 图片生成/图生图/学生妹Qwen2512真实人像质感御姐美女_2040753602402197506.json, 图片生成/图生图/局部重绘-QWen-Image-Instantx-Controlnet_1966292208708128769.json, 图片生成/图生图/局部重绘-QWen-Image-Instantx-Controlnet_1971006146779717633.json, 图片生成/图生图/局部重绘-QWen-Image-Instantx-Controlnet_2028275236034060289.json, 图片生成/图生图/局部重绘-QWen-Image【Instantx-Controlnet】_1966421780745400322.json, 图片生成/图生图/居家美女Qwen2512真实人像质感御姐美女_2040768961993773057.json, 图片生成/图生图/巷子印花少女Qwen2512真实人像质感御姐美女_2040771081161674754.json, 图片生成/图生图/异域风情雪山Qwen2512真实人像质感御姐美女_2040745153714982913.json, 图片生成/图生图/性感女讲师Qwen2512真实人像质感御姐美女_2040762674857910273.json, 图片生成/图生图/性感有韵味Qwen2512真实人像质感御姐美女_2040758880275275777.json, 图片生成/图生图/成熟有气质Qwen2512真实人像质感御姐美女_2040713629946880002.json, 图片生成/图生图/扩图重绘-QWen-Image-Instantx-Controlnet_1966296641936461825.json, 图片生成/图生图/扩图重绘-千问-Image-【Instantx-Controlnet】_1966428766404816897.json, 图片生成/图生图/调色局部重绘-QWen-Image-Instantx-Controlnet_2026552365544902657.json, 图片生成/文生图/局部重绘_1968599107654832130.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_4

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（图片生成/图生图/东方阳台美女Qwen2512真实人像质感御姐美女_2040720553853591554.json、图片生成/图生图/中文文字重绘-QWen-Image-Instantx-Controlnet_1966363579702259713.json、图片生成/图生图/人物换背景-QWen-Image-Instantx-Controlnet_1966295550452822018.json、图片生成/图生图/俯视户外Qwen2512真实人像质感御姐美女_2040701228971200514.json、图片生成/图生图/古风美女Qwen2512真实人像质感御姐美女_2040756043898163202.json…）

- **类型**：Image To Image
- **样本数**：23
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 23 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Note _O` —— 13/23 个有
- `scale` —— 13/23 个有
- `ControlNetInpaintingAliMamaApply` —— 10/23 个有
- `ControlNetLoader` —— 10/23 个有
- `ImageAndMaskPreview` —— 10/23 个有
- `ImageStitch` —— 10/23 个有
- `PreviewImage` —— 10/23 个有
- `ImagePadForOutpaint` —— 2/23 个有
- `InvertMask` —— 1/23 个有
- `MaskPreview` —— 1/23 个有
- `easy imageRemBg` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 23 | 28% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 23 | 55% |
| 采样算法 | euler | - | 23 | 100% |
| 调度器 | beta | - | 23 | 57% |
| 重绘幅度 | 0.5 | 0.5 - 1 | 23 | 65% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/23 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，23 个样本，取值分散，一致性仅 28%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，23 个样本
- 采样算法 最常用 euler，23 个样本，一致性 100%
- 调度器 最常用 beta，23 个样本，一致性 57%
- 重绘幅度 中位数 0.5，观测区间 0.5 - 1，23 个样本
- 高发问题（13/23 个样本）：Steps较低可能导致细节不足

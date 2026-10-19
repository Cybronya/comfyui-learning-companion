---
name: text_to_image_lora_sampler_clip_20
type: Text To Image
frequency: 19
level: strong
coverage: 0.889895
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, CR Prompt Text]
members: [图片生成/图生图/2102487881666351105.json, 图片生成/图生图/2102506921529004033.json, 图片生成/图生图/2102517800026861570.json, 图片生成/图生图/2102520964331425794.json, 图片生成/图生图/2102528994515181569.json, 图片生成/图生图/2102540105742372865.json, 图片生成/图生图/2102541742317850626.json, 图片生成/图生图/2102597696380030977.json, 图片生成/图生图/2102603964750581761.json, 图片生成/图生图/2102626840547516418.json, 图片生成/图生图/2102634269028999170.json, 图片生成/图生图/2102640016362139650.json, 图片生成/图生图/2105864806925430785.json, 图片生成/图生图/Qwen Image 2.1一键扩图图生图工作流，图生图写实扩图处理工具_2107231075868172290.json, 图片生成/图生图/Qwen Image 2.1精准抠图工作流指哪扣哪交互式图生图体验，图生图抠图工具_2107258835344904194.json, 视频生成/图生视频/Qwen-Image-2.1一键扩图图生图｜写实风格扩展轻松搞定_2107980380883214337.json, 视频生成/图生视频/Qwen_Image_2.1一键图片换装图生图，人物服饰替换处理工具_2104382452906156034.json, 视频生成/图生视频/Qwen_Image_2.1图片换头换脸，一键面部替换的图生图处理工具_2106546399436431361.json, 视频生成/图生视频/qwen_image2.1多图编辑进阶版｜文生图图生图自由切换｜批量改图高效_2104446242880315393.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_20

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/2102487881666351105.json、图片生成/图生图/2102506921529004033.json、图片生成/图生图/2102517800026861570.json、图片生成/图生图/2102520964331425794.json、图片生成/图生图/2102528994515181569.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 18/19 个有
- `TextEncodeQwenImage21` —— 18/19 个有
- `ComfySwitchNode` —— 16/19 个有
- `ResolutionSelector` —— 15/19 个有
- `孤海注释` —— 14/19 个有
- `BatchImagesNode` —— 11/19 个有
- `TextGenerateLTX2Prompt` —— 11/19 个有
- `EmptyImage` —— 6/19 个有
- `PreviewImage` —— 6/19 个有
- `CR Text` —— 3/19 个有
- `ImageStitch` —— 3/19 个有
- `SaveImageAdvanced` —— 3/19 个有
- `PrimitiveBoolean` —— 2/19 个有
- `Anything Everywhere3` —— 1/19 个有
- `CR Prompt Text` —— 1/19 个有
- `Float` —— 1/19 个有
- `JDCN_StringToList` —— 1/19 个有
- `RH_RhartImageG2ImageToImage` —— 1/19 个有
- `RTXVideoSuperResolution` —— 1/19 个有
- `easy showAnything` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 19 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 19 | 100% |
| 采样算法 | er_sde | - | 19 | 100% |
| 调度器 | beta | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |
| 宽度 | 80 | 80 - 80 | 19 | 100% |
| 高度 | 80 | 80 - 80 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，19 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，19 个样本，一致性 100%
- 调度器 最常用 beta，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 高发问题（21/19 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR Prompt Text

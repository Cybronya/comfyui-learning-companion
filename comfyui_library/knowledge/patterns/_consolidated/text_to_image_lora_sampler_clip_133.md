---
name: text_to_image_lora_sampler_clip_133
type: Text To Image
frequency: 11
level: strong
coverage: 0.877727
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1多图编辑工作流，支持保留人物姿势换服饰等多图参考场景_2102833574943744001.json, 图片生成/图生图/Qwen Image 2.1多图编辑工作流｜角色一致性轻松保｜批量改图不跑脸_2102623788155363330.json, 图片生成/图生图/Qwen Image 2.1多图编辑提示词增强in 版图生图处理工具_2102480198032781314.json, 图片生成/图生图/Qwen Image 2.1多图编辑文生图图生图处理工具_2102505314745667586.json, 图片生成/图生图/Qwen Image 2.1多图编辑｜多张参考图合并编辑出图_2108046219019898882.json, 图片生成/图生图/Qwen Image 2.1多图编辑｜多张素材融合处理一步到位_2107681855259627522.json, 图片生成/图生图/Qwen Image 2.1多宫格分镜图V2图生图处理工具_2102559055175835650.json, 图片生成/图生图/Qwen Image 2.1多宫格分镜图V2，图生图快速产出多格故事板方案_2103263596930232322.json, 图片生成/图生图/Qwen image 2.1 turbo图生图 快速改图直出方案_2110353791806697473.json, 图片生成/图生图/Qwen image 2.1多宫格分镜图V2.2 多场景批量出图方案_2105381690167349250.json, 视频生成/图生视频/Qwen_Image_2.1多图编辑工作流，支持保留人物姿势换服饰等多图参考场景_2106172420255207425.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_133

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1多图编辑工作流，支持保留人物姿势换服饰等多图参考场景_2102833574943744001.json、图片生成/图生图/Qwen Image 2.1多图编辑工作流｜角色一致性轻松保｜批量改图不跑脸_2102623788155363330.json、图片生成/图生图/Qwen Image 2.1多图编辑提示词增强in 版图生图处理工具_2102480198032781314.json、图片生成/图生图/Qwen Image 2.1多图编辑文生图图生图处理工具_2102505314745667586.json、图片生成/图生图/Qwen Image 2.1多图编辑｜多张参考图合并编辑出图_2108046219019898882.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 10/11 个有
- `ResolutionSelector` —— 10/11 个有
- `孤海注释` —— 10/11 个有
- `QwenImage21Cache` —— 9/11 个有
- `easy showAnything` —— 9/11 个有
- `BatchImagesNode` —— 8/11 个有
- `PrimitiveStringMultiline` —— 8/11 个有
- `PrimitiveBoolean` —— 5/11 个有
- `Fast Groups Bypasser (rgthree)` —— 3/11 个有
- `Fast Groups Muter (rgthree)` —— 3/11 个有
- `RHLLMChatNode` —— 3/11 个有
- `StringConcatenate` —— 3/11 个有
- `ZNGB_ImageBatchMulti` —— 3/11 个有
- `ImageMergeNode` —— 2/11 个有
- `CR Text` —— 1/11 个有
- `EmptyImage` —— 1/11 个有
- `JDCN_StringToList` —— 1/11 个有
- `KSamplerSelect` —— 1/11 个有
- `ManualSigmas` —— 1/11 个有
- `PreviewImage` —— 1/11 个有
- `SamplerCustom` —— 1/11 个有
- `SaveImageAdvanced` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（13/11 个样本）：Steps较低可能导致细节不足

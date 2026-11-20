---
name: text_to_image_lora_sampler_clip_116
type: Text To Image
frequency: 13
level: strong
coverage: 0.885154
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/flux3_klien3文生图，人像写真平面设计出图_2111559376304693250.json, 图片生成/文生图/文生图工作流｜即梦图片4.6中文文字精准生成_2100836535871557633.json, 视频生成/图生视频/H3导演台批量短剧专用4到9宫图视频生成_2100304059428331521.json, 视频生成/图生视频/H3导演台批量短剧专用4到9宫图视频生成工具_2100683233586401281.json, 视频生成/图生视频/MiniMax H3 Ref2AV bf16 lightx2v八步加速V2工作流，图生视频方案_2106095744552886273.json, 视频生成/图生视频/MiniMax H3全参官方指南自动扩展提示词T6工作流，角色一致性图生视频_2106097208906043393.json, 视频生成/图生视频/MiniMax H3全参官方指南自动扩展提示词，角色表演图生视频工作流_2103588976929099778.json, 视频生成/图生视频/MiniMax H3全参连续帧提示词自动优化工作流，图生视频高效创作方案_2106094286554099714.json, 视频生成/图生视频/Ref2AV八步加速V2｜MInimaxH3 bf16-lightx2v图生视频_2094721166920478721.json, 视频生成/图生视频/T6全参官方指南｜minimaxh3自动扩展提示词分镜出图_2094333256052334594.json, 视频生成/图生视频/T8全参官方指南｜minimaxh3扩展提示词角色一致性生视频_2094463893199482882.json, 视频生成/图生视频/minimaxh3全参官方指南自动扩展提示词_2086537843907846146.json, 视频生成/图生视频/全参连续帧优化｜minimaxh3提示词自动图生视频生成_2094719853226717186.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_116

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/flux3_klien3文生图，人像写真平面设计出图_2111559376304693250.json、图片生成/文生图/文生图工作流｜即梦图片4.6中文文字精准生成_2100836535871557633.json、视频生成/图生视频/H3导演台批量短剧专用4到9宫图视频生成_2100304059428331521.json、视频生成/图生视频/H3导演台批量短剧专用4到9宫图视频生成工具_2100683233586401281.json、视频生成/图生视频/MiniMax H3 Ref2AV bf16 lightx2v八步加速V2工作流，图生视频方案_2106095744552886273.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 12/13 个有
- `KSamplerSelect` —— 12/13 个有
- `RandomNoise` —— 12/13 个有
- `SamplerCustomAdvanced` —— 12/13 个有
- `BasicScheduler` —— 11/13 个有
- `LoadImage` —— 11/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 11/13 个有
- `VAEDecodeAudio` —— 11/13 个有
- `VHS_VideoCombine` —— 11/13 个有
- `ResolutionSelector` —— 9/13 个有
- `Text` —— 9/13 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 9/13 个有
- `RHHiddenNodes` —— 8/13 个有
- `SaveImage` —— 8/13 个有
- `ComfyMathExpression` —— 7/13 个有
- `ImageConcatenateMulti_UTK` —— 7/13 个有
- `PreviewImage` —— 7/13 个有
- `PrimitiveFloat` —— 7/13 个有
- `LoraLoaderBypassModelOnly` —— 4/13 个有
- `PrimitiveStringMultiline` —— 4/13 个有
- `easy showAnything` —— 3/13 个有
- `EnhancedLoadDiffusionModel` —— 2/13 个有
- `LoadAudio` —— 2/13 个有
- `SFH3MultimodalDirector` —— 2/13 个有
- `easy imageSplitGrid` —— 2/13 个有
- `easy indexAnything` —— 2/13 个有
- `Int` —— 1/13 个有
- `ManualSigmas` —— 1/13 个有
- `RH_BytedanceJimeng46TextToImage` —— 1/13 个有
- `RH_Captioner` —— 1/13 个有
- `RH_Translator` —— 1/13 个有
- `TextConcatenate_UTK` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（14/13 个样本）：Steps较低可能导致细节不足

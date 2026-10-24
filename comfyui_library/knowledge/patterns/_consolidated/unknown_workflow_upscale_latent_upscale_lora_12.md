---
name: unknown_workflow_upscale_latent_upscale_lora_12
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.841875
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/文生视频/LTX-2 文生视频适配LoRA 1080P_2073300625739313153.json, 视频生成/文生视频/LTX-2.3  文生视频 MV视频_2037159958583709697.json, 视频生成/文生视频/LTX-2.3-T2V-文生音视频_2029816055798964226.json, 视频生成/文生视频/LTX-2.3-图生视频_文生视频_2030340655863570434.json, 视频生成/文生视频/LTX-2.3-文生视频 长视频_2032729674383626241.json, 视频生成/文生视频/LTX-2.3-文生视频_2031191268642004993.json, 视频生成/文生视频/LTX-2.3-文生视频_2037040523202007042.json, 视频生成/文生视频/LTX2 文生视频原版自动提示词_2008719056999813121.json, 视频生成/文生视频/LTX2.3  图生视频  超强开源视频模型_2044752658199744513.json, 视频生成/文生视频/LTX2.3 图生视频 音画同步   万能图生视频 优化加速版_2030092123399262210.json, 视频生成/文生视频/LTX2.3 文生视频 v1.1+VBVR_2030533262598213634.json, 视频生成/文生视频/LTX2.3 文生视频_2029978568398213122.json, 视频生成/文生视频/LTX2.3 文生视频工作流_2029878986880327681.json, 视频生成/文生视频/LTX2.3 文生视频工作流_2031938415188516866.json, 视频生成/文生视频/LTX2.3-文生视频_2066069178989240321.json, 视频生成/文生视频/LTX2.3图生视频—最佳效果_2062858202403926018.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_12

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/文生视频/LTX-2 文生视频适配LoRA 1080P_2073300625739313153.json、视频生成/文生视频/LTX-2.3  文生视频 MV视频_2037159958583709697.json、视频生成/文生视频/LTX-2.3-T2V-文生音视频_2029816055798964226.json、视频生成/文生视频/LTX-2.3-图生视频_文生视频_2030340655863570434.json、视频生成/文生视频/LTX-2.3-文生视频 长视频_2032729674383626241.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 16 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `LTXVScheduler` —— 15/16 个有
- `PreviewAny` —— 15/16 个有
- `TextGenerateLTX2Prompt` —— 14/16 个有
- `DualCLIPLoader` —— 13/16 个有
- `KSampler` —— 13/16 个有
- `PrimitiveFloat` —— 13/16 个有
- `VAEDecode` —— 13/16 个有
- `VAEDecodeTiled` —— 13/16 个有
- `LTXVImgToVideoInplace` —— 4/16 个有
- `LTXVPreprocess` —— 4/16 个有
- `LoadImage` —— 4/16 个有
- `ResizeImageMaskNode` —— 4/16 个有
- `ResizeImagesByLongerEdge` —— 4/16 个有
- `ManualSigmas` —— 3/16 个有
- `CR Prompt Text` —— 2/16 个有
- `Text` —— 2/16 个有
- `easy cleanGpuUsed` —— 2/16 个有
- `intToFloat _O` —— 2/16 个有
- `Fast Groups Bypasser (rgthree)` —— 1/16 个有
- `Int` —— 1/16 个有
- `PreviewImage` —— 1/16 个有
- `PrimitiveStringMultiline` —— 1/16 个有
- `PurgeVRAM_UTK` —— 1/16 个有
- `RH_LLMAPI_NODE` —— 1/16 个有
- `RH_LLMAPI_Pro_Node` —— 1/16 个有
- `Seed (rgthree)` —— 1/16 个有
- `ShowAnything|Mie` —— 1/16 个有
- `SimpleMath+` —— 1/16 个有
- `Switch` —— 1/16 个有
- `Wan_video_prompt_generator` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 16 | 100% |
| 高度 | 25 | 25 - 25 | 16 | 100% |
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 0.4 | 0.25 - 0.4 | 13 | 89% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/16 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，16 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，16 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.25 - 0.4，13 个样本，取值集中（一致性 89%）
- 高发问题（14/16 个样本）：Steps较低可能导致细节不足

---
name: unknown_workflow_upscale_latent_upscale_lora_12
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.837143
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/文生视频/LTX-2 文生视频适配LoRA 1080P_2073300625739313153.json, 视频生成/文生视频/LTX-2.3  文生视频 MV视频_2037159958583709697.json, 视频生成/文生视频/LTX-2.3-T2V-文生音视频_2029816055798964226.json, 视频生成/文生视频/LTX-2.3-文生视频 长视频_2032729674383626241.json, 视频生成/文生视频/LTX-2.3-文生视频_2030171248226996226.json, 视频生成/文生视频/LTX-2.3-文生视频_2031191268642004993.json, 视频生成/文生视频/LTX-2.3-文生视频_2037040523202007042.json, 视频生成/文生视频/LTX-2文生视频ComfyUI官方流快速ltx2模型fp8加速模型带音效_2012003240623218689.json, 视频生成/文生视频/LTX-2文生视频Plus运行模式专用_2008537121744752642.json, 视频生成/文生视频/LTX-2文生视频工作流_2008796662071824386.json, 视频生成/文生视频/LTX-2文生视频工作流_2009245499412455426.json, 视频生成/文生视频/LTX-2文生视频提示词优化版_2009586018684510210.json, 视频生成/文生视频/LTX2 文生视频原版自动提示词_2008719056999813121.json, 视频生成/文生视频/LTX2.0-低显存版-自动提示词-动态强化-运镜加速-文生视频V1_2011665816391000065.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_12

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/文生视频/LTX-2 文生视频适配LoRA 1080P_2073300625739313153.json、视频生成/文生视频/LTX-2.3  文生视频 MV视频_2037159958583709697.json、视频生成/文生视频/LTX-2.3-T2V-文生音视频_2029816055798964226.json、视频生成/文生视频/LTX-2.3-文生视频 长视频_2032729674383626241.json、视频生成/文生视频/LTX-2.3-文生视频_2030171248226996226.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 14 个 workflow 都包含：
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
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `LTXVScheduler` —— 13/14 个有
- `PrimitiveFloat` —— 13/14 个有
- `PrimitiveInt` —— 13/14 个有
- `ManualSigmas` —— 9/14 个有
- `PreviewAny` —— 7/14 个有
- `VAEDecode` —— 7/14 个有
- `KSampler` —— 5/14 个有
- `TextGenerateLTX2Prompt` —— 5/14 个有
- `DualCLIPLoader` —— 4/14 个有
- `easy cleanGpuUsed` —— 4/14 个有
- `CR Prompt Text` —— 3/14 个有
- `RH_LLMAPI_Pro_Node` —— 3/14 个有
- `Int` —— 2/14 个有
- `Label (rgthree)` —— 2/14 个有
- `LayerUtility: PurgeVRAM V2` —— 2/14 个有
- `SimpleMath+` —— 2/14 个有
- `AddLabel` —— 1/14 个有
- `Any To Any` —— 1/14 个有
- `JWInteger` —— 1/14 个有
- `JoinStrings` —— 1/14 个有
- `PrimitiveStringMultiline` —— 1/14 个有
- `PurgeVRAM_UTK` —— 1/14 个有
- `Qwen3_VQA` —— 1/14 个有
- `RH_LLMAPI_NODE` —— 1/14 个有
- `ShowAnything|Mie` —— 1/14 个有
- `Switch` —— 1/14 个有
- `TextInput_` —— 1/14 个有
- `Textbox` —— 1/14 个有
- `VRAMReserver` —— 1/14 个有
- `Wan_video_prompt_generator` —— 1/14 个有
- `easy anythingIndexSwitch` —— 1/14 个有
- `intToFloat _O` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 14 | 100% |
| 高度 | 25 | 25 - 25 | 14 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 0.4 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/14 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，14 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，14 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.4，5 个样本，取值集中（一致性 100%）

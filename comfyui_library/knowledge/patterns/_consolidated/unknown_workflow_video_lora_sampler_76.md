---
name: unknown_workflow_video_lora_sampler_76
type: Unknown Workflow
frequency: 17
level: strong
coverage: 0.913
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DF_Integer, ImageStitch, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, RH_Translator, SimpleMath+, UNETLoader, VAEDecode, VAELoader, WanFirstLastFrameToVideo, WanVideoNAG, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1957688772295061505.json, 视频生成/图生视频/1957693851249078273.json, 视频生成/图生视频/1954885586667520002.json, 视频生成/图生视频/1952219642674753538.json, 视频生成/图生视频/1952339456634368002.json, 视频生成/图生视频/1970093575075733506.json, 视频生成/图生视频/1956153773183959042.json, 视频生成/图生视频/1962136836984475650.json, 视频生成/图生视频/1951973819386900481.json, 视频生成/图生视频/1952239777980600322.json, 视频生成/图生视频/1952981780628443138.json, 视频生成/图生视频/1967782938588884994.json, 视频生成/图生视频/2004156685763731458.json, 视频生成/图生视频/2015306300099403777.json, 视频生成/图生视频/2054766656261500930.json, 视频生成/图生视频/2055193435040165889.json, 视频生成/图生视频/2072861343484567553.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_76

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/1957688772295061505.json、视频生成/图生视频/1957693851249078273.json、视频生成/图生视频/1954885586667520002.json、视频生成/图生视频/1952219642674753538.json、视频生成/图生视频/1952339456634368002.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DF_Integer`
- `ImageStitch`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `RH_Translator`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanFirstLastFrameToVideo`
- `WanVideoNAG`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 16/17 个有
- `PathchSageAttentionKJ` —— 16/17 个有
- `RH_Captioner` —— 16/17 个有
- `LayerUtility: ImageMaskScaleAs` —— 15/17 个有
- `PrimitiveBoolean` —— 15/17 个有
- `Textbox` —— 15/17 个有
- `easy ifElse` —— 15/17 个有
- `CreateVideo` —— 14/17 个有
- `SaveVideo` —— 14/17 个有
- `VHS_VideoCombine` —— 4/17 个有
- `CR Image Size` —— 1/17 个有
- `CR Prompt Text` —— 1/17 个有
- `CustomAddLabel` —— 1/17 个有
- `Float` —— 1/17 个有
- `GetNode` —— 1/17 个有
- `HunyuanVideoFoley` —— 1/17 个有
- `ImageUpscaleWithModel` —— 1/17 个有
- `Int` —— 1/17 个有
- `LayerUtility: PurgeVRAM V2` —— 1/17 个有
- `NormalizeAudioLoudness` —— 1/17 个有
- `PlaySound|pysssss` —— 1/17 个有
- `RHHiddenNodes` —— 1/17 个有
- `SetNode` —— 1/17 个有
- `UpscaleModelLoader` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 17 | 94% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 17 | 100% |
| 采样算法 | 4 | 1 - 4 | 17 | 82% |
| 调度器 | euler | - | 17 | 94% |
| 重绘幅度 | simple | - | 17 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，17 个样本，一致性 94%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，17 个样本，取值集中（一致性 100%）
- 采样算法 中位数 4，观测区间 1 - 4，17 个样本，取值集中（一致性 82%）
- 调度器 最常用 euler，17 个样本，一致性 94%
- 重绘幅度 最常用 simple，17 个样本，一致性 100%

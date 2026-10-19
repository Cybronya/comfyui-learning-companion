---
name: unknown_workflow_controlnet_lora_sampler_3
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.855333
common_nodes: [AIO_Preprocessor, BasicGuider, BasicScheduler, CLIPTextEncode, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, FluxGuidance, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetUnionControlNetType, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, easy cleanGpuUsed, Text Concatenate, Text Multiline, CR Text]
members: [图片生成/文生图/1912691278339895298.json, 图片生成/文生图/1913100134115409921.json, 图片生成/文生图/1921750937419857922.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_3

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1912691278339895298.json、图片生成/文生图/1913100134115409921.json、图片生成/文生图/1921750937419857922.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetUnionControlNetType`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ApplyFBCacheOnModel` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `ApplyIPAdapterFlux` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `DownloadAndLoadFlorence2Model` —— 1/3 个有
- `EmptyLatentImage` —— 1/3 个有
- `Florence2Run` —— 1/3 个有
- `IPAdapterFluxLoader` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `RepeatLatentBatch` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `Text Concatenate` —— 1/3 个有
- `Text Multiline` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |
| ControlNet 权重 | 0.8 | 0.8 - 0.8 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.8，观测区间 0.8 - 0.8，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、easy cleanGpuUsed、Text Concatenate、Text Multiline、CR Text

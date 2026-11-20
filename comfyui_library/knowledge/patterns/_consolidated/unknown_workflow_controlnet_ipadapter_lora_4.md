---
name: unknown_workflow_controlnet_ipadapter_lora_4
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.649667
common_nodes: [ACN_AdvancedControlNetApplySingle_v2, AIO_Preprocessor, ApplyIPAdapterFlux, BasicGuider, BasicScheduler, CLIPTextEncodeFlux, CR Text Concatenate, DualCLIPLoader, IPAdapterFluxLoader, Image Comparer (rgthree), KSamplerSelect, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, TextInput_, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, workflow>1, workflow>2]
problems: []
missing: []
members: [图片生成/图生图/一键照片风格化-多重控制V1（详细讲解使用）_1975109291587842049.json, 平台全量/【一键】照片风格换转+曼陀罗华_麦橘超然_V1风格_1953256662268317697.json, 平台全量/一键照片风格化-多重控制V1（详细讲解使用）_1911663559552528385.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_ipadapter_lora_4

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/一键照片风格化-多重控制V1（详细讲解使用）_1975109291587842049.json、平台全量/【一键】照片风格换转+曼陀罗华_麦橘超然_V1风格_1953256662268317697.json、平台全量/一键照片风格化-多重控制V1（详细讲解使用）_1911663559552528385.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 3 个 workflow 都包含：
- `ACN_AdvancedControlNetApplySingle_v2`
- `AIO_Preprocessor`
- `ApplyIPAdapterFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncodeFlux`
- `CR Text Concatenate`
- `DualCLIPLoader`
- `IPAdapterFluxLoader`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `workflow>1`
- `workflow>2`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 2/3 个有
- `EmptyLatentImage` —— 2/3 个有
- `ImageResizeKJ` —— 2/3 个有
- `Joy_caption_two` —— 2/3 个有
- `Joy_caption_two_load` —— 2/3 个有
- `CR Simple Image Compare` —— 1/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `LayerUtility: GetImageSize` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/3 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.3 | 0.3 - 0.3 | 3 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1536 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.3，观测区间 0.3 - 0.3，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，样本不足，未给区间，2 个样本，取值集中（一致性 100%）

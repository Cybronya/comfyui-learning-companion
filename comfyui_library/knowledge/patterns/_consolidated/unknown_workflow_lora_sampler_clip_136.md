---
name: unknown_workflow_lora_sampler_clip_136
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.83525
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ConstrainImage|pysssss, EmptySD3LatentImage, FluxGuidance, GetImageSize+, ImageConcatFromBatch, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingFlux, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, StyleModelApply, StyleModelLoader, VAEDecode, easy imageSplitGrid, easy imagesSplitImage]
problems: []
missing: []
members: [图片生成/图生图/FLUX电商多视角一致性_1911786902012526593.json, 图片生成/图生图/FLUX电商多视角一致性（自动拆分）_1916392178686562306.json, 图片生成/图生图/多视角一致性_1905447368635125761.json, 图片生成/图生图/小红书人物一致性9宫格文生图工作流_1916514021267144705.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_136

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/FLUX电商多视角一致性_1911786902012526593.json、图片生成/图生图/FLUX电商多视角一致性（自动拆分）_1916392178686562306.json、图片生成/图生图/多视角一致性_1905447368635125761.json、图片生成/图生图/小红书人物一致性9宫格文生图工作流_1916514021267144705.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ConstrainImage|pysssss`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `GetImageSize+`
- `ImageConcatFromBatch`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `StyleModelApply`
- `StyleModelLoader`
- `VAEDecode`
- `easy imageSplitGrid`
- `easy imagesSplitImage`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadFlorence2Model` —— 3/4 个有
- `Florence2Run` —— 3/4 个有
- `SDVN Joy Caption` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

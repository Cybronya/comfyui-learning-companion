---
name: unknown_workflow_sampler_clip_checkpoint_21
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8332
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, LoadImage, ModelSamplingFlux, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, StyleModelApply, StyleModelLoader, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/FLUX电商多视角一致性_1911786902012526593.json, 图片生成/图生图/FLUX电商多视角一致性（自动拆分）_1916392178686562306.json, 图片生成/图生图/多视角一致性_1905447368635125761.json, 图片生成/图生图/小红书人物一致性9宫格文生图工作流_1916514021267144705.json, 平台全量/Pokemon Workflow 3.0 (flux redux)_1863785483770740738.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_21

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/FLUX电商多视角一致性_1911786902012526593.json、图片生成/图生图/FLUX电商多视角一致性（自动拆分）_1916392178686562306.json、图片生成/图生图/多视角一致性_1905447368635125761.json、图片生成/图生图/小红书人物一致性9宫格文生图工作流_1916514021267144705.json、平台全量/Pokemon Workflow 3.0 (flux redux)_1863785483770740738.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `StyleModelApply`
- `StyleModelLoader`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ConstrainImage|pysssss` —— 4/5 个有
- `DownloadAndLoadFlorence2Model` —— 4/5 个有
- `Florence2Run` —— 4/5 个有
- `GetImageSize+` —— 4/5 个有
- `ImageConcatFromBatch` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `easy imageSplitGrid` —— 4/5 个有
- `easy imagesSplitImage` —— 4/5 个有
- `CR Text` —— 1/5 个有
- `LayerUtility: TextJoin` —— 1/5 个有
- `OllamaGenerate` —— 1/5 个有
- `Replace Text _O` —— 1/5 个有
- `SDVN Joy Caption` —— 1/5 个有
- `SDXLAspectRatioSelector` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

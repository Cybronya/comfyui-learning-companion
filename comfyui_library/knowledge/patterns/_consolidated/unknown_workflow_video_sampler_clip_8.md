---
name: unknown_workflow_video_sampler_clip_8
type: Unknown Workflow
frequency: 30
level: strong
coverage: 0.7716
common_nodes: [CLIPLoader, CLIPTextEncode, ImageScaleBy, JWInteger, KSamplerAdvanced, ModelSamplingSD3, Pick From Batch (mtb), PreviewImage, PrimitiveStringMultiline, RIFE VFI, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything]
problems: []
missing: [Label (rgthree), LogicGateNegateValue, MathExpression|pysssss, Pick From Batch (mtb), RIFE VFI, Text Concatenate, easy cleanGpuUsed, Seed (rgthree)]
members: [视频生成/图生视频/1979750970857000961.json, 视频生成/图生视频/1982291012414513154.json, 视频生成/图生视频/1979768280627974145.json, 视频生成/图生视频/1989386587425394690.json, 视频生成/图生视频/1984913774840856578.json, 视频生成/图生视频/1979719907665416194.json, 视频生成/图生视频/1979748437547716610.json, 视频生成/图生视频/1989386607084138498.json, 视频生成/图生视频/1979784514803240961.json, 视频生成/图生视频/1984048201416245250.json, 视频生成/图生视频/1984848712461598721.json, 视频生成/图生视频/1984539603493404673.json, 视频生成/图生视频/1981294869803073538.json, 视频生成/图生视频/1990048747956654082.json, 视频生成/图生视频/1990423185483063298.json, 视频生成/图生视频/1982292381343072258.json, 视频生成/图生视频/1982290285344497666.json, 视频生成/图生视频/1979770513943859201.json, 视频生成/图生视频/1979752163389902850.json, 视频生成/图生视频/2046037420713451522.json, 视频生成/图生视频/1987142608080318466.json, 视频生成/图生视频/2059074218825965569.json, 视频生成/图生视频/1980114227547508737.json, 视频生成/文生视频/1979696533400621058.json, 视频生成/文生视频/Smooth Mix Wan 2.2：文生视频_1989368083322163201.json, 视频生成/文生视频/Smooth Mix Wan 2.2：文生视频（流畅如丝，内置补帧）_1984903672830312450.json, 视频生成/文生视频/Smooth Mix Wan 2.2：文生视频，流畅如丝，细节如画！_2013566157537681410.json, 视频生成/文生视频/Smooth Mix Wan 2.2：文生视频，流畅如丝，细节如画！_2013815011306643457.json, 视频生成/文生视频/Smooth Mix Wan 2.2：文生视频，高质量生成_2006002817242447874.json, 视频生成/文生视频/Smooth+Mix+Wan+2.2：文生视频，高质量 流畅视频_2009979362870824961.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_8

> 由 `engine/knowledge_consolidation` 从 30 个 workflow 归纳得出（视频生成/图生视频/1979750970857000961.json、视频生成/图生视频/1982291012414513154.json、视频生成/图生视频/1979768280627974145.json、视频生成/图生视频/1989386587425394690.json、视频生成/图生视频/1984913774840856578.json…）

- **类型**：Unknown Workflow
- **样本数**：30
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 30 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageScaleBy`
- `JWInteger`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `Pick From Batch (mtb)`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RIFE VFI`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `MathExpression|pysssss` —— 27/30 个有
- `ModelPatchTorchSettings` —— 27/30 个有
- `PathchSageAttentionKJ` —— 27/30 个有
- `Text Concatenate` —— 27/30 个有
- `wanBlockSwap` —— 27/30 个有
- `ImpactSwitch` —— 26/30 个有
- `Wan22PromptSelector` —— 26/30 个有
- `RH_LLMAPI_NODE` —— 25/30 个有
- `LoadImage` —— 24/30 个有
- `WanImageToVideo` —— 24/30 个有
- `CLIPVisionEncode` —— 23/30 个有
- `CLIPVisionLoader` —— 23/30 个有
- `Label (rgthree)` —— 19/30 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 18/30 个有
- `ShowText` —— 18/30 个有
- `ImageResizeKJv2` —— 8/30 个有
- `LogicGateNegateValue` —— 7/30 个有
- `WanFirstLastFrameToVideo` —— 5/30 个有
- `CR Prompt Text` —— 3/30 个有
- `ColorMatch` —— 3/30 个有
- `StringConcatenate` —— 3/30 个有
- `LoraLoaderModelOnly` —— 2/30 个有
- `Bjornulf_ShowInt` —— 1/30 个有
- `PainterI2V` —— 1/30 个有
- `Qwen3_VQA` —— 1/30 个有
- `RH_Captioner` —— 1/30 个有
- `ShowText|pysssss` —— 1/30 个有
- `SimpleMath+` —— 1/30 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 30 | 73% |
| Prompt 约束强度(CFG) | 10 | 8 - 10 | 30 | 94% |
| 采样算法 | 1 | 1 - 1 | 30 | 100% |
| 调度器 | euler_ancestral | - | 30 | 93% |
| 重绘幅度 | simple | - | 30 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，30 个样本，一致性 73%
- Prompt 约束强度(CFG) 中位数 10，观测区间 8 - 10，30 个样本，取值集中（一致性 94%）
- 采样算法 中位数 1，观测区间 1 - 1，30 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，30 个样本，一致性 93%
- 重绘幅度 最常用 simple，30 个样本，一致性 100%
- 这些节点还没有知识卡，系统对它们的理解有限：Label (rgthree)、LogicGateNegateValue、MathExpression|pysssss、Pick From Batch (mtb)、RIFE VFI

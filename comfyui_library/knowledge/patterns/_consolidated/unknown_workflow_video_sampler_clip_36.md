---
name: unknown_workflow_video_sampler_clip_36
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.767429
common_nodes: [CLIPLoader, CLIPTextEncode, ImageScaleBy, JWInteger, KSamplerAdvanced, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, Pick From Batch (mtb), PrimitiveStringMultiline, RIFE VFI, Seed (rgthree), UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/Wan 2.2 Smooth Mix + Foley：图生视频（音画同步）_2036101580507844609.json, 视频生成/图生视频/Wan 2.2 Smooth Mix：图生视频（动作流畅，无色差）_1986816558620209154.json, 视频生成/图生视频/【Wan2.2】丝滑图生视频 Smooth Mix Wan 2.2_1979770513943859201.json, 视频生成/图生视频/【图生视频】Smooth Mix Wan 2.2_1979752163389902850.json, 视频生成/图生视频/【图生视频】Wan 2.2_2046037420713451522.json, 视频生成/图生视频/首尾帧驱动，AI自动补全叙事(Smooth Mix Wan 2.2)_1987142608080318466.json, 视频生成/图生视频/首尾帧驱动，AI自动补全叙事(Smooth Mix Wan 2.2)_2059074218825965569.json, 视频生成/文生视频/Smooth Mix Wan 2.2：文生视频_1989368083322163201.json, 视频生成/文生视频/Smooth Mix Wan 2.2：文生视频（流畅如丝，内置补帧）_1984903672830312450.json, 视频生成/文生视频/Smooth Mix Wan 2.2：文生视频，流畅如丝，细节如画！_1979696533400621058.json, 视频生成/文生视频/Smooth Mix Wan 2.2：文生视频，流畅如丝，细节如画！_2013566157537681410.json, 视频生成/文生视频/Smooth Mix Wan 2.2：文生视频，流畅如丝，细节如画！_2013815011306643457.json, 视频生成/文生视频/Smooth Mix Wan 2.2：文生视频，高质量生成_2006002817242447874.json, 视频生成/文生视频/Smooth+Mix+Wan+2.2：文生视频，高质量 流畅视频_2009979362870824961.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_36

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/Wan 2.2 Smooth Mix + Foley：图生视频（音画同步）_2036101580507844609.json、视频生成/图生视频/Wan 2.2 Smooth Mix：图生视频（动作流畅，无色差）_1986816558620209154.json、视频生成/图生视频/【Wan2.2】丝滑图生视频 Smooth Mix Wan 2.2_1979770513943859201.json、视频生成/图生视频/【图生视频】Smooth Mix Wan 2.2_1979752163389902850.json、视频生成/图生视频/【图生视频】Wan 2.2_2046037420713451522.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageScaleBy`
- `JWInteger`
- `KSamplerAdvanced`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `Pick From Batch (mtb)`
- `PrimitiveStringMultiline`
- `RIFE VFI`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 13/14 个有
- `SaveImage` —— 13/14 个有
- `ImpactSwitch` —— 12/14 个有
- `RH_LLMAPI_NODE` —— 12/14 个有
- `Text Concatenate` —— 12/14 个有
- `Wan22PromptSelector` —— 12/14 个有
- `WanImageToVideo` —— 12/14 个有
- `Label (rgthree)` —— 8/14 个有
- `LoadImage` —— 8/14 个有
- `CLIPVisionEncode` —— 7/14 个有
- `CLIPVisionLoader` —— 7/14 个有
- `LogicGateNegateValue` —— 7/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/14 个有
- `ShowText` —— 5/14 个有
- `ImageResizeKJv2` —— 2/14 个有
- `WanFirstLastFrameToVideo` —— 2/14 个有
- `AudioAdjustVolume` —— 1/14 个有
- `Bool` —— 1/14 个有
- `ConvertAny2Float` —— 1/14 个有
- `EmptyAudio` —— 1/14 个有
- `HunyuanVideoFoley` —— 1/14 个有
- `PreviewAudio` —— 1/14 个有
- `RH_Translator` —— 1/14 个有
- `easy ifElse` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 14 | 50% |
| Prompt 约束强度(CFG) | 10 | 10 - 10 | 14 | 100% |
| 采样算法 | 1 | 1 - 1 | 14 | 100% |
| 调度器 | euler_ancestral | - | 14 | 100% |
| 重绘幅度 | simple | - | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，14 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 10，观测区间 10 - 10，14 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，14 个样本，一致性 100%
- 重绘幅度 最常用 simple，14 个样本，一致性 100%

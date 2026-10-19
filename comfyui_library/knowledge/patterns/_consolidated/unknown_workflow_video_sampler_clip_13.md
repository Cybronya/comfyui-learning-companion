---
name: unknown_workflow_video_sampler_clip_13
type: Unknown Workflow
frequency: 22
level: strong
coverage: 0.797182
common_nodes: [CLIPLoader, CLIPTextEncode, JoinStrings, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, Qwen3_VQA, VAEDecode, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2008070467520827394.json, 视频生成/图生视频/2008456378490298370.json, 视频生成/图生视频/2014552922826219521.json, 视频生成/图生视频/2012098237326434305.json, 视频生成/图生视频/2021468643665645570.json, 视频生成/图生视频/2013628693922455554.json, 视频生成/图生视频/2008911916491608065.json, 视频生成/图生视频/2007697248326520833.json, 视频生成/图生视频/2012911713028415489.json, 视频生成/图生视频/2043636549258055682.json, 视频生成/图生视频/2051946371376267266.json, 视频生成/图生视频/2056991338461229058.json, 视频生成/图生视频/2019973370779013122.json, 视频生成/图生视频/2016351598326321154.json, 视频生成/图生视频/2017586752311005186.json, 视频生成/图生视频/2019702921687998465.json, 视频生成/图生视频/2055193382787526658.json, 视频生成/图生视频/2046496638318944258.json, 视频生成/文生视频/WAN2.2 DaSiWaV9  最强动漫视频生成（提示词优化版）_2083117546869444609.json, 视频生成/文生视频/最强动漫视频生成DaSiWaV9_2013204639008694274.json, 视频生成/文生视频/最强动漫视频生成DaSiWaV9_支持单图+_首尾帧+_+三图首尾帧_2045146603354333186.json, 视频生成/文生视频/超自然动漫图生视频DaSiWaV9支持单图+_首尾帧+_三图_2034443299951480833.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_13

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（视频生成/图生视频/2008070467520827394.json、视频生成/图生视频/2008456378490298370.json、视频生成/图生视频/2014552922826219521.json、视频生成/图生视频/2012098237326434305.json、视频生成/图生视频/2021468643665645570.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 22 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `JoinStrings`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `Qwen3_VQA`
- `VAEDecode`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 21/22 个有
- `Int` —— 21/22 个有
- `TextInput_` —— 21/22 个有
- `UNETLoader` —— 20/22 个有
- `VAELoader` —— 20/22 个有
- `PainterI2V` —— 19/22 个有
- `RIFE VFI` —— 19/22 个有
- `ShowText|pysssss` —— 19/22 个有
- `SimpleMath+` —— 19/22 个有
- `ImageConcatMulti` —— 18/22 个有
- `WanFirstLastFrameToVideo` —— 18/22 个有
- `PrimitiveInt` —— 16/22 个有
- `ImageBatchMulti` —— 15/22 个有
- `ImageResizeKJv2` —— 15/22 个有
- `WanMultiFrameRefToVideo` —— 15/22 个有
- `Fast Groups Muter (rgthree)` —— 14/22 个有
- `GetImagesFromBatchIndexed` —— 7/22 个有
- `Fast Groups Bypasser (rgthree)` —— 6/22 个有
- `easy convertAnything` —— 4/22 个有
- `LoraLoaderModelOnly` —— 2/22 个有
- `RHHiddenNodes` —— 2/22 个有
- `TextListSplit` —— 1/22 个有
- `easy positive` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 22 | 68% |
| Prompt 约束强度(CFG) | 6 | 4 - 6 | 22 | 80% |
| 采样算法 | 1 | 1 - 1 | 22 | 100% |
| 调度器 | euler | - | 22 | 100% |
| 重绘幅度 | simple | - | 22 | 86% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，22 个样本，一致性 68%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 6，22 个样本，取值集中（一致性 80%）
- 采样算法 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，22 个样本，一致性 100%
- 重绘幅度 最常用 simple，22 个样本，一致性 86%

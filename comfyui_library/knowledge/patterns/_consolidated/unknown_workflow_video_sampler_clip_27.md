---
name: unknown_workflow_video_sampler_clip_27
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.751375
common_nodes: [CLIPLoader, CLIPTextEncode, ImageConcatMulti, JoinStrings, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchTorchSettings, PathchSageAttentionKJ, Qwen3_VQA, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/动漫首尾帧_Wan2.2_DaSiWa8.1_2021468643665645570.json, 视频生成/图生视频/双图首尾帧+动漫真人通用-电影质感动漫DaSiWaV9_2013628693922455554.json, 视频生成/图生视频/图生视频 最强视频生成 首尾三图首尾帧_2031688685132976129.json, 视频生成/图生视频/图生视频-WAN2.2 DaSiWaV9  最强动漫视频生成（提示词优化版）_2070316679850188801.json, 视频生成/图生视频/图生视频-老照片动起来_2085169884861919234.json, 视频生成/图生视频/图生视频三图生成_2044969480081641474.json, 视频生成/图生视频/图生视频流-支持单图 _ 双图 _ 三图 出视频（最高支持五图）_1993305632644284418.json, 视频生成/图生视频/最强动漫图生视频DaSiWaV9_支持单图 _首尾帧 _三图_2026126514126852097.json, 视频生成/图生视频/最强动漫模型DaSiWa8.1视频流 浮云1.19_2013098243374190593.json, 视频生成/图生视频/最强动漫模型DaSiWa8.1视频流-支持单图 _双图 _ 三图 出视频_2007697248326520833.json, 视频生成/图生视频/最强动漫模型DaSiWa8.1首帧中间帧和尾帧出视频_2009925117761032194.json, 视频生成/图生视频/最强动漫视频生成DaSiWaV9_支持单图 _首尾帧 _ 三图首尾帧_2012911713028415489.json, 视频生成/图生视频/最强动漫视频生成DaSiWaV9_支持单图 _首尾帧 _ 三图首尾帧_2043636549258055682.json, 视频生成/图生视频/最强动漫视频生成DaSiWaV9_支持单图 _首尾帧 _ 三图首尾帧_2051946371376267266.json, 视频生成/图生视频/最强动漫视频生成DaSiWaV9_支持单图 _首尾帧 _ 三图首尾帧_2056991338461229058.json, 视频生成/图生视频/最强动漫视频生成DaSiWaV9_支持单图_首尾帧_三图首尾帧_2113549545073373186.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_27

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/动漫首尾帧_Wan2.2_DaSiWa8.1_2021468643665645570.json、视频生成/图生视频/双图首尾帧+动漫真人通用-电影质感动漫DaSiWaV9_2013628693922455554.json、视频生成/图生视频/图生视频 最强视频生成 首尾三图首尾帧_2031688685132976129.json、视频生成/图生视频/图生视频-WAN2.2 DaSiWaV9  最强动漫视频生成（提示词优化版）_2070316679850188801.json、视频生成/图生视频/图生视频-老照片动起来_2085169884861919234.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageConcatMulti`
- `JoinStrings`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `Qwen3_VQA`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Int` —— 15/16 个有
- `RIFE VFI` —— 15/16 个有
- `TextInput_` —— 15/16 个有
- `ImageBatchMulti` —— 14/16 个有
- `ImageResizeKJv2` —— 14/16 个有
- `PreviewImage` —— 14/16 个有
- `WanMultiFrameRefToVideo` —— 14/16 个有
- `INTConstant` —— 13/16 个有
- `ModelSamplingSD3` —— 13/16 个有
- `PrimitiveInt` —— 13/16 个有
- `WanFirstLastFrameToVideo` —— 13/16 个有
- `easy cleanGpuUsed` —— 12/16 个有
- `PainterI2V` —— 11/16 个有
- `SimpleMath+` —— 11/16 个有
- `Fast Groups Muter (rgthree)` —— 8/16 个有
- `GetImagesFromBatchIndexed` —— 5/16 个有
- `Fast Groups Bypasser (rgthree)` —— 4/16 个有
- `EmptyImage` —— 1/16 个有
- `LoraLoaderModelOnly` —— 1/16 个有
- `RH_LLMAPI_NODE` —— 1/16 个有
- `TextListSplit` —— 1/16 个有
- `easy positive` —— 1/16 个有
- `wanBlockSwap` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 16 | 69% |
| Prompt 约束强度(CFG) | 5 | 4 - 6 | 16 | 80% |
| 采样算法 | 1 | 1 - 1 | 16 | 100% |
| 调度器 | euler | - | 16 | 100% |
| 重绘幅度 | simple | - | 16 | 81% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，16 个样本，一致性 69%
- Prompt 约束强度(CFG) 中位数 5，观测区间 4 - 6，16 个样本，取值集中（一致性 80%）
- 采样算法 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，16 个样本，一致性 100%
- 重绘幅度 最常用 simple，16 个样本，一致性 81%

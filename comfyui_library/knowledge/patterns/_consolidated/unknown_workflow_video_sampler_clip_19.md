---
name: unknown_workflow_video_sampler_clip_19
type: Unknown Workflow
frequency: 20
level: strong
coverage: 0.75835
common_nodes: [CLIPLoader, CLIPTextEncode, ImageConcatMulti, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchTorchSettings, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/动漫首尾帧_Wan2.2_DaSiWa8.1_2021468643665645570.json, 视频生成/图生视频/双图首尾帧+动漫真人通用-电影质感动漫DaSiWaV9_2013628693922455554.json, 视频生成/图生视频/图生视频 最强视频生成 首尾三图首尾帧_2031688685132976129.json, 视频生成/图生视频/图生视频-WAN2.2 DaSiWaV9  最强动漫视频生成（提示词优化版）_2070316679850188801.json, 视频生成/图生视频/图生视频-老照片动起来_2085169884861919234.json, 视频生成/图生视频/图生视频三图生成_2044969480081641474.json, 视频生成/图生视频/图生视频流-支持单图 _ 双图 _ 三图 出视频（最高支持五图）_1993305632644284418.json, 视频生成/图生视频/最强动漫图生视频DaSiWaV9_支持单图 _首尾帧 _三图_2026126514126852097.json, 视频生成/图生视频/最强动漫模型DaSiWa8.1视频流 浮云1.19_2013098243374190593.json, 视频生成/图生视频/最强动漫模型DaSiWa8.1视频流-支持单图 _双图 _ 三图 出视频_2007697248326520833.json, 视频生成/图生视频/最强动漫模型DaSiWa8.1首帧中间帧和尾帧出视频_2009925117761032194.json, 视频生成/图生视频/最强动漫视频生成DaSiWaV9_支持单图 _首尾帧 _ 三图首尾帧_2012911713028415489.json, 视频生成/图生视频/最强动漫视频生成DaSiWaV9_支持单图 _首尾帧 _ 三图首尾帧_2043636549258055682.json, 视频生成/图生视频/最强动漫视频生成DaSiWaV9_支持单图 _首尾帧 _ 三图首尾帧_2051946371376267266.json, 视频生成/图生视频/最强动漫视频生成DaSiWaV9_支持单图 _首尾帧 _ 三图首尾帧_2056991338461229058.json, 视频生成/图生视频/最强动漫视频生成DaSiWaV9：支持单图、首尾帧及三图首尾帧创作工作流_2019973370779013122.json, 视频生成/图生视频/最强动漫视频生成支持单图+首尾帧_2016351598326321154.json, 视频生成/图生视频/最强短剧 动漫视频 生成DaSiWaV9_支持单图 _首尾帧 _ 三图首尾帧_2017586752311005186.json, 视频生成/图生视频/最强短剧 动漫视频 生成DaSiWaV9_支持单图 _首尾帧 _ 三图首尾帧_2019702921687998465.json, 视频生成/图生视频/液体滴落到产品上_2001566408855154689.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_19

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/动漫首尾帧_Wan2.2_DaSiWa8.1_2021468643665645570.json、视频生成/图生视频/双图首尾帧+动漫真人通用-电影质感动漫DaSiWaV9_2013628693922455554.json、视频生成/图生视频/图生视频 最强视频生成 首尾三图首尾帧_2031688685132976129.json、视频生成/图生视频/图生视频-WAN2.2 DaSiWaV9  最强动漫视频生成（提示词优化版）_2070316679850188801.json、视频生成/图生视频/图生视频-老照片动起来_2085169884861919234.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageConcatMulti`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Int` —— 19/20 个有
- `JoinStrings` —— 19/20 个有
- `Qwen3_VQA` —— 19/20 个有
- `RIFE VFI` —— 19/20 个有
- `ShowText|pysssss` —— 19/20 个有
- `TextInput_` —— 19/20 个有
- `easy showAnything` —— 19/20 个有
- `ImageBatchMulti` —— 18/20 个有
- `ImageResizeKJv2` —— 18/20 个有
- `PreviewImage` —— 18/20 个有
- `WanMultiFrameRefToVideo` —— 18/20 个有
- `INTConstant` —— 17/20 个有
- `ModelSamplingSD3` —— 17/20 个有
- `PrimitiveInt` —— 17/20 个有
- `WanFirstLastFrameToVideo` —— 17/20 个有
- `easy cleanGpuUsed` —— 16/20 个有
- `PainterI2V` —— 15/20 个有
- `SimpleMath+` —— 14/20 个有
- `Fast Groups Muter (rgthree)` —— 11/20 个有
- `GetImagesFromBatchIndexed` —— 6/20 个有
- `Fast Groups Bypasser (rgthree)` —— 5/20 个有
- `LoraLoaderModelOnly` —— 2/20 个有
- `RH_LLMAPI_NODE` —— 1/20 个有
- `TextListSplit` —— 1/20 个有
- `easy positive` —— 1/20 个有
- `ttN seed` —— 1/20 个有
- `wanBlockSwap` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 20 | 70% |
| Prompt 约束强度(CFG) | 6 | 4 - 6 | 20 | 80% |
| 采样算法 | 1 | 1 - 1 | 20 | 100% |
| 调度器 | euler | - | 20 | 100% |
| 重绘幅度 | simple | - | 20 | 85% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，20 个样本，一致性 70%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 6，20 个样本，取值集中（一致性 80%）
- 采样算法 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，20 个样本，一致性 100%
- 重绘幅度 最常用 simple，20 个样本，一致性 85%

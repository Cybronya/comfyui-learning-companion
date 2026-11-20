---
name: unknown_workflow_video_sampler_clip_28
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.895533
common_nodes: [CLIPLoader, CLIPTextEncode, Int, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/DaSiWa8.1-Wan2.2双图参考首尾帧AI漫剧_2010412985205923842.json, 视频生成/图生视频/DaSiWa8.1-Wan2.2双图参考首尾帧AI漫剧_2010413439973330946.json, 视频生成/图生视频/大丝袜DasiwaWAN22漫剧专用图生视频_2010348801411780609.json, 视频生成/图生视频/大丝袜DasiwaWAN22漫剧专用图生视频_2010386931812667393.json, 视频生成/图生视频/电影质感+动漫视频+单图版（DaSiWaV9 WAN2.single image）_2013251284761059330.json, 视频生成/图生视频/电影质感动漫视频生成DaSiWaV9 -三图生视频-首帧+中间帧+尾帧-自动提示词_2023651384347860994.json, 视频生成/图生视频/电影质感动漫视频生成DaSiWaV9 -单图生视频-自动提示词_2023419797345669121.json, 视频生成/图生视频/电影质感动漫视频生成DaSiWaV9 -双图首尾帧视频-自动提示词_2023632584692994049.json, 视频生成/图生视频/真人动漫视频生成DaSiWaV9_支持单图 _首尾帧 _ 三图首尾帧_2055193382787526658.json, 视频生成/图生视频/首尾帧视频-无提示词_2025278485094211586.json, 视频生成/图生视频/🔥超好用🔥动漫视频生成-支持单图 -首尾帧 -三图首尾帧_2046496638318944258.json, 视频生成/文生视频/WAN2.2 DaSiWaV9  最强动漫视频生成（提示词优化版）_2083117546869444609.json, 视频生成/文生视频/最强动漫视频生成DaSiWaV9_2013204639008694274.json, 视频生成/文生视频/最强动漫视频生成DaSiWaV9_支持单图+_首尾帧+_+三图首尾帧_2045146603354333186.json, 视频生成/文生视频/超自然动漫图生视频DaSiWaV9支持单图+_首尾帧+_三图_2034443299951480833.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_28

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/DaSiWa8.1-Wan2.2双图参考首尾帧AI漫剧_2010412985205923842.json、视频生成/图生视频/DaSiWa8.1-Wan2.2双图参考首尾帧AI漫剧_2010413439973330946.json、视频生成/图生视频/大丝袜DasiwaWAN22漫剧专用图生视频_2010348801411780609.json、视频生成/图生视频/大丝袜DasiwaWAN22漫剧专用图生视频_2010386931812667393.json、视频生成/图生视频/电影质感+动漫视频+单图版（DaSiWaV9 WAN2.single image）_2013251284761059330.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Int`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ModelPatchTorchSettings` —— 14/15 个有
- `ModelSamplingSD3` —— 14/15 个有
- `PathchSageAttentionKJ` —— 14/15 个有
- `easy cleanGpuUsed` —— 14/15 个有
- `PainterI2V` —— 12/15 个有
- `RIFE VFI` —— 12/15 个有
- `INTConstant` —— 11/15 个有
- `ImageConcatMulti` —— 11/15 个有
- `JoinStrings` —— 11/15 个有
- `Qwen3_VQA` —— 11/15 个有
- `ShowText|pysssss` —— 11/15 个有
- `TextInput_` —— 11/15 个有
- `WanFirstLastFrameToVideo` —— 8/15 个有
- `ImageBatchMulti` —— 7/15 个有
- `ImageResizeKJv2` —— 7/15 个有
- `PreviewImage` —— 7/15 个有
- `PrimitiveInt` —— 7/15 个有
- `WanMultiFrameRefToVideo` —— 7/15 个有
- `Fast Groups Muter (rgthree)` —— 6/15 个有
- `CR Text` —— 4/15 个有
- `PrimitiveString` —— 4/15 个有
- `RHHiddenNodes` —— 4/15 个有
- `CustomAddLabel` —— 3/15 个有
- `LoraLoaderModelOnly` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 15 | 100% |
| Prompt 约束强度(CFG) | 6 | 4 - 6 | 15 | 81% |
| 采样算法 | 1 | 1 - 1 | 15 | 100% |
| 调度器 | euler | - | 15 | 100% |
| 重绘幅度 | simple | - | 15 | 87% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，15 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 6，15 个样本，取值集中（一致性 81%）
- 采样算法 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，15 个样本，一致性 100%
- 重绘幅度 最常用 simple，15 个样本，一致性 87%

---
name: unknown_workflow_video_sampler_clip_54
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.544364
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2首尾帧生视频_2042865188126334978.json, 视频生成/图生视频/修改自WorkFIsher大佬的工作流-首尾帧视频-需自己便携提示词-更精准控制视频_2011676327186796545.json, 视频生成/图生视频/可加描述的首尾帧视频WAN2.2-RemixV2__I2V_2032355101955858434.json, 视频生成/图生视频/提示词高度遵守，动态效果很好_1983516962250760194.json, 视频生成/图生视频/最强逻辑首尾祯_1999623009306636290.json, 视频生成/图生视频/最新首尾帧WAN2.2-RemixV2-I2V图生视频集合版_1988509206477234177.json, 视频生成/图生视频/水墨风朗诵背景山水视频制作思路_2068956549908881410.json, 视频生成/图生视频/短剧制作-WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度_1984186286053474306.json, 视频生成/图生视频/简单点wan2.2-remixv2-i2v图生视频_2044709107302670338.json, 视频生成/图生视频/超好用WAN2.2-LightX2V-I2V_2010308124921569281.json, 视频生成/图生视频/首尾帧-WAN2.2-RemixV2-I2V_2006524559020789762.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_54

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/wan2.2首尾帧生视频_2042865188126334978.json、视频生成/图生视频/修改自WorkFIsher大佬的工作流-首尾帧视频-需自己便携提示词-更精准控制视频_2011676327186796545.json、视频生成/图生视频/可加描述的首尾帧视频WAN2.2-RemixV2__I2V_2032355101955858434.json、视频生成/图生视频/提示词高度遵守，动态效果很好_1983516962250760194.json、视频生成/图生视频/最强逻辑首尾祯_1999623009306636290.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：54%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Int` —— 10/11 个有
- `PreviewImage` —— 10/11 个有
- `RIFE VFI` —— 10/11 个有
- `easy cleanGpuUsed` —— 10/11 个有
- `INTConstant` —— 9/11 个有
- `LoadImage` —— 9/11 个有
- `wanBlockSwap` —— 9/11 个有
- `Fast Groups Bypasser (rgthree)` —— 8/11 个有
- `WanImageToVideo` —— 7/11 个有
- `ImageResizeKJv2` —— 6/11 个有
- `WanFirstLastFrameToVideo` —— 6/11 个有
- `LoraLoaderModelOnly` —— 5/11 个有
- `ImageLoader` —— 4/11 个有
- `SaveImage` —— 2/11 个有
- `DuckHideNode` —— 1/11 个有
- `Fast Bypasser (rgthree)` —— 1/11 个有
- `GetImagesFromBatchIndexed` —— 1/11 个有
- `ImageFromBatch` —— 1/11 个有
- `easy imageScaleDownToSize` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 11 | 64% |
| Prompt 约束强度(CFG) | 4 | 4 - 6 | 11 | 82% |
| 采样算法 | 1 | 1 - 1 | 11 | 100% |
| 调度器 | euler | - | 11 | 100% |
| 重绘幅度 | normal | - | 11 | 91% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，11 个样本，一致性 64%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 6，11 个样本，取值集中（一致性 82%）
- 采样算法 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，11 个样本，一致性 100%
- 重绘幅度 最常用 normal，11 个样本，一致性 91%

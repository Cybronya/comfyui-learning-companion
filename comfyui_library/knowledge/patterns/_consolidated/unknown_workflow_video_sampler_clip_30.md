---
name: unknown_workflow_video_sampler_clip_30
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.521133
common_nodes: [CLIPLoader, CLIPTextEncode, Int, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: ["视频生成/图生视频/video_图生视频WAN2.2-LightX2V-I2V一镜到底,超强动态，高质量，高遵循度API_2006247037502758914.json", 视频生成/图生视频/video_图生视频WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度API_1999107369680371713.json, 视频生成/图生视频/video_首尾帧WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度API_2000487723846729730.json, 视频生成/图生视频/video_首尾帧WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度API_2006292810990882817.json, 视频生成/图生视频/wan2.2图生视频——高动态高遵循度_2055902519104163842.json, 视频生成/图生视频/修改自WorkFIsher大佬的工作流-首尾帧视频-需自己便携提示词-更精准控制视频_2011676327186796545.json, 视频生成/图生视频/图生视频自动切镜头WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度API_2003771509095211009.json, 视频生成/图生视频/提示词高度遵守，动态效果很好_1983516962250760194.json, 视频生成/图生视频/最强逻辑首尾祯_1999623009306636290.json, 视频生成/图生视频/最新首尾帧WAN2.2-RemixV2-I2V图生视频集合版_1988509206477234177.json, 视频生成/图生视频/水墨风朗诵背景山水视频制作思路_2068956549908881410.json, 视频生成/图生视频/短剧制作-WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度_1984186286053474306.json, 视频生成/图生视频/简单点wan2.2-remixv2-i2v图生视频_2044709107302670338.json, 视频生成/图生视频/超好用WAN2.2-LightX2V-I2V_2010308124921569281.json, 视频生成/图生视频/首尾帧-WAN2.2-RemixV2-I2V_2006524559020789762.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_30

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/video_图生视频WAN2.2-LightX2V-I2V一镜到底,超强动态，高质量，高遵循度API_2006247037502758914.json、视频生成/图生视频/video_图生视频WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度API_1999107369680371713.json、视频生成/图生视频/video_首尾帧WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度API_2000487723846729730.json、视频生成/图生视频/video_首尾帧WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度API_2006292810990882817.json、视频生成/图生视频/wan2.2图生视频——高动态高遵循度_2055902519104163842.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：52%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Int`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 14/15 个有
- `LoadImage` —— 14/15 个有
- `WanImageToVideo` —— 13/15 个有
- `wanBlockSwap` —— 13/15 个有
- `Fast Groups Bypasser (rgthree)` —— 12/15 个有
- `LoraLoaderModelOnly` —— 11/15 个有
- `RIFE VFI` —— 10/15 个有
- `PreviewImage` —— 9/15 个有
- `WanFirstLastFrameToVideo` —— 6/15 个有
- `PrimitiveStringMultiline` —— 5/15 个有
- `easy int` —— 5/15 个有
- `ImageResizeKJv2` —— 4/15 个有
- `ImageLoader` —— 3/15 个有
- `SaveImage` —— 2/15 个有
- `DuckHideNode` —— 1/15 个有
- `Fast Bypasser (rgthree)` —— 1/15 个有
- `Fast Groups Muter (rgthree)` —— 1/15 个有
- `GetImagesFromBatchIndexed` —— 1/15 个有
- `ImageFromBatch` —— 1/15 个有
- `easy imageScaleDownToSize` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 15 | 87% |
| Prompt 约束强度(CFG) | 4 | 4 - 6 | 15 | 88% |
| 采样算法 | 1 | 1 - 1 | 15 | 100% |
| 调度器 | euler | - | 15 | 100% |
| 重绘幅度 | normal | - | 15 | 93% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，15 个样本，一致性 87%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 6，15 个样本，取值集中（一致性 88%）
- 采样算法 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，15 个样本，一致性 100%
- 重绘幅度 最常用 normal，15 个样本，一致性 93%

---
name: unknown_workflow_video_sampler_clip_53
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.825182
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, Fast Groups Bypasser (rgthree), INTConstant, ImageResizeKJv2, Int, LoadImage, ModelPatchTorchSettings, PathchSageAttentionKJ, RIFE VFI, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanMoeKSampler, easy cleanGpuUsed, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/11FINAL-Qwen3VL 图生视频_2049387851611119618.json, 视频生成/图生视频/2026 SmoothPro图片生视频_2009138591993171970.json, 视频生成/图生视频/Edit V5版全能自动分镜（视频加首尾）_1979025771903750146.json, 视频生成/图生视频/Qwen3VL+首尾帧视频生成_2049389424517058561.json, 视频生成/图生视频/WANSmooth Mix  万相图生视频 首尾帧 新增加角色迁移 优化部署_2011360351337586690.json, 视频生成/图生视频/Wan2.2_Smooth Mix I2V图生视频合集_2003656092246786049.json, 视频生成/图生视频/Wan2.2_Smooth+Mix+I2V图生视频_2008710367467278338.json, 视频生成/图生视频/Work-Fisher-Edit Next Scene（自动分镜）-V1版_1978804615628099585.json, 视频生成/图生视频/首尾视频Wan2.2_Smooth Mix I2V_1978131739417665538.json, 视频生成/文生视频/AI视频制作神器 自动连续分镜Next Scene V1.0版_1979224907714301953.json, 视频生成/文生视频/动漫短剧AI视频制作神器——自动连续分镜Next Scene-V1版_1978956982134673409.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_53

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/11FINAL-Qwen3VL 图生视频_2049387851611119618.json、视频生成/图生视频/2026 SmoothPro图片生视频_2009138591993171970.json、视频生成/图生视频/Edit V5版全能自动分镜（视频加首尾）_1979025771903750146.json、视频生成/图生视频/Qwen3VL+首尾帧视频生成_2049389424517058561.json、视频生成/图生视频/WANSmooth Mix  万相图生视频 首尾帧 新增加角色迁移 优化部署_2011360351337586690.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `RIFE VFI`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanMoeKSampler`
- `easy cleanGpuUsed`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `DF_Integer` —— 10/11 个有
- `SimpleMath+` —— 10/11 个有
- `WanFirstLastFrameToVideo` —— 10/11 个有
- `WanImageToVideo` —— 9/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/11 个有
- `CheckpointLoaderSimple` —— 4/11 个有
- `ConditioningZeroOut` —— 4/11 个有
- `KSampler` —— 4/11 个有
- `LoraLoaderModelOnly` —— 4/11 个有
- `SaveImage` —— 4/11 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 4/11 个有
- `easy promptLine` —— 4/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 11 | 55% |
| Prompt 约束强度(CFG) | 8 | 1 - 8 | 11 | 48% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | 1 | 1 - 1 | 8 | 100% |
| 重绘幅度 | euler_ancestral | - | 11 | 73% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，11 个样本，一致性 55%
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 8，11 个样本，取值分散，一致性仅 48%
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler_ancestral，11 个样本，一致性 73%

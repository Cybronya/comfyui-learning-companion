---
name: unknown_workflow_video_sampler_clip_31
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.808333
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, Fast Groups Bypasser (rgthree), INTConstant, ImageResizeKJv2, Int, LoadImage, ModelPatchTorchSettings, PathchSageAttentionKJ, RIFE VFI, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanMoeKSampler, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/11FINAL-Qwen3VL 图生视频_2049387851611119618.json, 视频生成/图生视频/2026 SmoothPro图片生视频_2009138591993171970.json, 视频生成/图生视频/Edit V5版全能自动分镜（视频加首尾）_1979025771903750146.json, 视频生成/图生视频/Qwen3VL+首尾帧视频生成_2049389424517058561.json, 视频生成/图生视频/WANSmooth Mix  万相图生视频 首尾帧 新增加角色迁移 优化部署_2011360351337586690.json, 视频生成/图生视频/Wan2.2_Smooth Mix I2V图生视频合集_2003656092246786049.json, 视频生成/图生视频/Wan2.2_Smooth+Mix+I2V图生视频_2008710367467278338.json, 视频生成/图生视频/Wan2.2_Smooth_I2V_1978100410332372994.json, 视频生成/图生视频/Work-Fisher-Edit Next Scene（自动分镜）-V1版_1978804615628099585.json, 视频生成/图生视频/Work-Fisher_Wan2.2_Smooth Mix I2V_1977733586520526849.json, 视频生成/图生视频/升帧率版！视频更流畅！SmoothMix图生视频工作流_2041940547862011906.json, 视频生成/图生视频/图生视频三合一_1989202915321589761.json, 视频生成/图生视频/首尾帧_图生视频四合一_1992859603580899330.json, 视频生成/文生视频/AI视频制作神器 自动连续分镜Next Scene V1.0版_1979224907714301953.json, 视频生成/文生视频/动漫短剧AI视频制作神器——自动连续分镜Next Scene-V1版_1978956982134673409.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_31

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/11FINAL-Qwen3VL 图生视频_2049387851611119618.json、视频生成/图生视频/2026 SmoothPro图片生视频_2009138591993171970.json、视频生成/图生视频/Edit V5版全能自动分镜（视频加首尾）_1979025771903750146.json、视频生成/图生视频/Qwen3VL+首尾帧视频生成_2049389424517058561.json、视频生成/图生视频/WANSmooth Mix  万相图生视频 首尾帧 新增加角色迁移 优化部署_2011360351337586690.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 15 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `DF_Integer` —— 14/15 个有
- `SimpleMath+` —— 14/15 个有
- `wanBlockSwap` —— 13/15 个有
- `WanFirstLastFrameToVideo` —— 12/15 个有
- `WanImageToVideo` —— 12/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/15 个有
- `LoraLoaderModelOnly` —— 6/15 个有
- `CheckpointLoaderSimple` —— 4/15 个有
- `ConditioningZeroOut` —— 4/15 个有
- `KSampler` —— 4/15 个有
- `SaveImage` —— 4/15 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 4/15 个有
- `easy promptLine` —— 4/15 个有
- `FL_RIFE` —— 2/15 个有
- `KSamplerAdvanced` —— 2/15 个有
- `ModelSamplingSD3` —— 2/15 个有
- `PreviewImage` —— 2/15 个有
- `ImageLoader` —— 1/15 个有
- `PlaySound|pysssss` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 15 | 47% |
| Prompt 约束强度(CFG) | 6 | 1 - 8 | 15 | 52% |
| 采样算法 | 1 | 1 - 1 | 12 | 100% |
| 调度器 | 1 | 1 - 1 | 10 | 100% |
| 重绘幅度 | euler_ancestral | - | 15 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，15 个样本，一致性 47%
- Prompt 约束强度(CFG) 中位数 6，观测区间 1 - 8，15 个样本
- 采样算法 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler_ancestral，15 个样本，一致性 67%

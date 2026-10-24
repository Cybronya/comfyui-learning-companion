---
name: unknown_workflow_video_clip_unet
type: Unknown Workflow
frequency: 26
level: moderate
coverage: 0.626731
common_nodes: [CLIPLoader, CLIPTextEncode, Fast Groups Bypasser (rgthree), INTConstant, Int, ModelPatchTorchSettings, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/11FINAL-Qwen3VL 图生视频_2049387851611119618.json, 视频生成/图生视频/2026 SmoothPro图片生视频_2009138591993171970.json, 视频生成/图生视频/Qwen3VL+首尾帧视频生成_2049389424517058561.json, 视频生成/图生视频/WAN2.2 RemixV2  I2V 图生视频_1996506562493554690.json, 视频生成/图生视频/WAN2.2 RemixV2  I2V 图生视频_2009254393203396610.json, 视频生成/图生视频/WAN2.2-RemixV2-I2V图生视频_2038989882521030658.json, 视频生成/图生视频/WAN2.2-RemixV2-I2V首尾帧丝滑变装转场_2009543545169907714.json, 视频生成/图生视频/WAN2.2-RemixV2-I2V首尾帧丝滑变装转场_2047592882332241922.json, 视频生成/图生视频/WAN2.2-RemixV2-I2V首尾帧丝滑变装转场_2051628991756419074.json, 视频生成/图生视频/WAN2.2-RemixV2-I2V首尾帧丝滑变装转场_2070382789744218114.json, 视频生成/图生视频/WAN2.2-RemixV2-I2V首尾帧视频_1987169484022681602.json, 视频生成/图生视频/WAN2.2-RemixV2__I2V首尾帧视频_2000107947743211522.json, 视频生成/图生视频/WAN2.2-RemixV2__I2V首尾帧视频_2014511689311461377.json, 视频生成/图生视频/WAN2.2高动态图生视频_2005870552181080066.json, 视频生成/图生视频/WANSmooth Mix  万相图生视频 首尾帧 新增加角色迁移 优化部署_2011360351337586690.json, 视频生成/图生视频/Wan2.2_Smooth Mix I2V图生视频_2014967936171118594.json, 视频生成/图生视频/Wan2.2_Smooth Mix I2V图生视频合集_2003656092246786049.json, 视频生成/图生视频/Wan2.2_Smooth+Mix+I2V图生视频_2008710367467278338.json, 视频生成/图生视频/Wan2.2_Smooth-Mix-I2V-常规图生视频和首尾帧生视频_1998270569793617921.json, 视频生成/图生视频/Wan2.2_Smooth_I2V_1978100410332372994.json, 视频生成/图生视频/Work-Fisher_Wan2.2_Smooth Mix I2V_1977733586520526849.json, 视频生成/图生视频/painterI2V_Smooth-Mix-I2V-动态强度可调版_1991393474855677954.json, 视频生成/图生视频/wan2.2 remix2.1动态增强版，图生视频，首尾帧_2016050718058221570.json, 视频生成/图生视频/升帧率版！视频更流畅！SmoothMix图生视频工作流_2041940547862011906.json, 视频生成/图生视频/图生视频三合一_1989202915321589761.json, 视频生成/图生视频/首尾帧_图生视频四合一_1992859603580899330.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（视频生成/图生视频/11FINAL-Qwen3VL 图生视频_2049387851611119618.json、视频生成/图生视频/2026 SmoothPro图片生视频_2009138591993171970.json、视频生成/图生视频/Qwen3VL+首尾帧视频生成_2049389424517058561.json、视频生成/图生视频/WAN2.2 RemixV2  I2V 图生视频_1996506562493554690.json、视频生成/图生视频/WAN2.2 RemixV2  I2V 图生视频_2009254393203396610.json…）

- **类型**：Unknown Workflow
- **样本数**：26
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 26 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `Int`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 25/26 个有
- `RIFE VFI` —— 25/26 个有
- `wanBlockSwap` —— 24/26 个有
- `LoadImage` —— 19/26 个有
- `WanFirstLastFrameToVideo` —— 17/26 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 16/26 个有
- `CLIPVisionEncode` —— 14/26 个有
- `CLIPVisionLoader` —— 14/26 个有
- `KSamplerAdvanced` —— 14/26 个有
- `ModelSamplingSD3` —— 14/26 个有
- `PreviewImage` —— 14/26 个有
- `WanImageToVideo` —— 14/26 个有
- `WanMoeKSampler` —— 14/26 个有
- `DF_Integer` —— 10/26 个有
- `SimpleMath+` —— 10/26 个有
- `ImageLoader` —— 9/26 个有
- `FL_RIFE` —— 2/26 个有
- `LoraLoaderModelOnly` —— 2/26 个有
- `PainterI2V` —— 2/26 个有
- `PlaySound|pysssss` —— 1/26 个有
- `PrimitiveStringMultiline` —— 1/26 个有
- `easy int` —— 1/26 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 26 | 65% |
| Prompt 约束强度(CFG) | 4 | 4 - 8 | 26 | 69% |
| 采样算法 | 1 | 1 - 1 | 26 | 100% |
| 调度器 | euler | - | 26 | 54% |
| 重绘幅度 | normal | - | 26 | 54% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，26 个样本，一致性 65%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 8，26 个样本
- 采样算法 中位数 1，观测区间 1 - 1，26 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，26 个样本，一致性 54%
- 重绘幅度 最常用 normal，26 个样本，一致性 54%

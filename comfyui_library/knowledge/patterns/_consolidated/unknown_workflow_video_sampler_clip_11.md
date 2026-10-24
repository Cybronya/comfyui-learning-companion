---
name: unknown_workflow_video_sampler_clip_11
type: Unknown Workflow
frequency: 25
level: strong
coverage: 0.75888
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ImageResizeKJv2, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Dasiwa I2V图生视频工作流 浮云1.28 更新_2016499156017221633.json, 视频生成/图生视频/Dasiwa I2V图生视频工作流 浮云1.28_2016457012112007170.json, 视频生成/图生视频/Remix V2 PainterI2V Plus版  浮云 头发动画 图生视频 12.11_1998932620186673154.json, 视频生成/图生视频/Remix V2 VS  Smooth图生视频对比工作流V4（PainterI2V Plus版）_1990820621133225985.json, 视频生成/图生视频/Remix V2 VS Lightx2v 1030 VS  Smooth图生视频对比工作流V1_1986358473883582465.json, 视频生成/图生视频/Remix V2 VS Lightx2v 1030 头发动画图生视频对比工作流V1 次用 浮云12_1998939454473691137.json, 视频生成/图生视频/Remix V2+PainterI2V图生视频自动提示词工作流V1（动态加强）_1987947016699449345.json, 视频生成/图生视频/Remix V2+PainterI2V图生视频自动提示词工作流V4（动态加强）_1991088759945146369.json, 视频生成/图生视频/Remix V2+PainterI2V图生视频（动态加强）1080P 5S 约14分开Plus48G_2001883203667390466.json, 视频生成/图生视频/Remix V2+PainterI2V高动态图生视频自动提示词_1993272567492444161.json, 视频生成/图生视频/Remix V2.1 UnifiedReward+VBVR多重对比I2V_2028082455047053313.json, 视频生成/图生视频/Remix V2.1+PainterI2V图生视频自动提示词工作流V1（一致性加强版）_2010957966706479106.json, 视频生成/图生视频/Remix V2.1+PainterI2V图生视频自动提示词工作流（一致性加强版）_2020428290829328386.json, 视频生成/图生视频/Remix V2.1图生视频V1（UnifiedReward+VBVR逻辑加强）_2028397486544527362.json, 视频生成/图生视频/Remix V2.1图生视频V1（UnifiedReward+VBVR逻辑加强）_2028678704204881921.json, 视频生成/图生视频/Remix V2.1图生视频V1（UnifiedReward+VBVR逻辑加强）_2028683653529735169.json, 视频生成/图生视频/Remix V2.1图生视频V1（UnifiedReward运动加强）_2028399847149146114.json, 视频生成/图生视频/Smooth +PainterI2V图生视频自动提示词工作流V2（Plus版）_1991085974646272001.json, 视频生成/图生视频/Smooth Mix+PainterI2V图生视频自动提示词工作流V1（动态加强）_1987947024861564930.json, 视频生成/图生视频/Wan2.2 VBVR精准逻辑推理图生视频V1_2025914003163189250.json, 视频生成/图生视频/【阿良绘】动漫强化图生视频_ Dasiwa V9+PainterI2V（简化）_2012167741138018306.json, 视频生成/图生视频/横版Remix V2 VS  Smooth图生视频对比工作流V2（PainterI2V Plus）_1991074720969891842.json, 视频生成/图生视频/视频-Remix V2.1建筑图生视频V1工作流_2029118702054023169.json, 视频生成/图生视频/（自用）Remix V2.1+PainterI2V图生视频自动提示词工作流V1（一致性加强版）_2011779085244047362.json, 视频生成/图生视频/（自用）Wan 2.2 Dasiwa +Animated 图生视频V1（双模式）_1991472801660018689.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_11

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（视频生成/图生视频/Dasiwa I2V图生视频工作流 浮云1.28 更新_2016499156017221633.json、视频生成/图生视频/Dasiwa I2V图生视频工作流 浮云1.28_2016457012112007170.json、视频生成/图生视频/Remix V2 PainterI2V Plus版  浮云 头发动画 图生视频 12.11_1998932620186673154.json、视频生成/图生视频/Remix V2 VS  Smooth图生视频对比工作流V4（PainterI2V Plus版）_1990820621133225985.json、视频生成/图生视频/Remix V2 VS Lightx2v 1030 VS  Smooth图生视频对比工作流V1_1986358473883582465.json…）

- **类型**：Unknown Workflow
- **样本数**：25
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 25 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 23/25 个有
- `ImageScaleBy` —— 23/25 个有
- `LayerUtility: PurgeVRAM` —— 23/25 个有
- `PathchSageAttentionKJ` —— 23/25 个有
- `Pick From Batch (mtb)` —— 23/25 个有
- `Seed (rgthree)` —— 23/25 个有
- `easy cleanGpuUsed` —— 23/25 个有
- `CR Prompt Text` —— 22/25 个有
- `PreviewImage` —— 22/25 个有
- `SaveImage` —— 22/25 个有
- `AILab_QwenVL` —— 20/25 个有
- `RunningHub Deepcleaner` —— 20/25 个有
- `easy showAnything` —— 20/25 个有
- `PainterI2V` —— 19/25 个有
- `RH_LLMAPI_NODE` —— 19/25 个有
- `Float` —— 18/25 个有
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1` —— 18/25 个有
- `easy anythingIndexSwitch` —— 17/25 个有
- `ImageFromBatch+` —— 14/25 个有
- `LoraLoaderModelOnly` —— 13/25 个有
- `MathExpression|pysssss` —— 13/25 个有
- `WanImageToVideo` —— 7/25 个有
- `AddLabel` —— 4/25 个有
- `ImageConcanate` —— 4/25 个有
- `PDIMAGE_LongerSize` —— 4/25 个有
- `Int` —— 2/25 个有
- `TT_img_enc` —— 2/25 个有
- `TT_img_enc_v2` —— 2/25 个有
- `ConcatTextOfUtils` —— 1/25 个有
- `DuckHideNode` —— 1/25 个有
- `ImageConcatMulti` —— 1/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 25 | 92% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 25 | 100% |
| 采样算法 | 1 | 1 - 1.5 | 25 | 87% |
| 调度器 | euler_ancestral | - | 25 | 88% |
| 重绘幅度 | simple | - | 25 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，25 个样本，一致性 92%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，25 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1.5，25 个样本，取值集中（一致性 87%）
- 调度器 最常用 euler_ancestral，25 个样本，一致性 88%
- 重绘幅度 最常用 simple，25 个样本，一致性 100%

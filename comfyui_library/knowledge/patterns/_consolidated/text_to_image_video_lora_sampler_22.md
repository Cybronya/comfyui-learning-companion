---
name: text_to_image_video_lora_sampler_22
type: Text To Image
frequency: 23
level: strong
coverage: 0.809
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/MiniMax H3 全参官方指南｜自动扩展提示词 T7 实测_2096823650333843458.json, 图片生成/图生图/MiniMax H3全参官方指南自动扩展提示词视频处理工具_2101006979501215745.json, 图片生成/图生图/MiniMax H3双图参考剧情短片｜有声视频叙事创作利器_2113555231446495233.json, 图片生成/图生图/MiniMax H3视频添加物品视频编辑，视频超分风格转换处理工具_2103899733600333826.json, 图片生成/图生图/MiniMaxH3视频添加物品编辑｜往已拍视频里塞新东西超简单_2103668392619237378.json, 图片生成/图生图/minimaxh3全参官方指南T7｜自动扩展提示词视频处理_2100784150339997697.json, 图片生成/图生图/全参官方指南T7｜minimaxh3自动扩展提示词处理_2093240407831437313.json, 图片生成/文生图/MiniMax H3 Ref2VA六图多参考角色一致性Sage加速文生图_2088251941397815297.json, 平台全量/视频换背景｜MiniMaxH3一句话修改视频背景_2099413858212470785.json, 数字人/数字人/Minimax H3多参考口播｜数字人口播素材多路喂｜口型和画面都对得上_2102653513489805313.json, 数字人/数字人/人物场景替换工作流｜数字人一键换背景搬家不穿帮_2097578172031258626.json, 数字人/数字人/优化版本新版口播方案，数字人视频生视频制作_2111284544136630274.json, 数字人/数字人/新版口播数字人视频生成工作流｜视频生视频一键出片_2108369479599218690.json, 视频生成/图生视频/H3视频换背景编辑 人物类特效处理生成工具_2100299115996467202.json, 视频生成/图生视频/H3视频换背景编辑工作流，人物特效背景替换自然融合高清直出_2115017314138677249.json, 视频生成/图生视频/MiniMax H3 FastVideo极速多参 视频生成加速方案_2109013584503201793.json, 视频生成/图生视频/MiniMax-H3视频编辑神器｜一键视频换背景人物类特效_2107652623632519170.json, 视频生成/图生视频/MiniMaxH3视频换背景编辑，视频生视频人物特效处理_2113101437289984001.json, 视频生成/图生视频/MiniMaxH3视频换背景，人物类特效视频生视频编辑器_2111274575668531202.json, 视频生成/图生视频/MiniMaxH3视频背景替换编辑，其它视频处理全能手_2111278750330605570.json, 视频生成/图生视频/MiniMax_H3视频换背景视频编辑工作流，人物类特效视频生视频处理工具_2109456422231699458.json, 视频生成/图生视频/MiniMax_H3视频换背景视频编辑工作流，人物类特效视频生视频处理方案_2109457359675412482.json, 视频生成/图生视频/首尾帧生成视频｜MiniMax H3官方工作流图生视频_2090268705291849730.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_22

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（图片生成/图生图/MiniMax H3 全参官方指南｜自动扩展提示词 T7 实测_2096823650333843458.json、图片生成/图生图/MiniMax H3全参官方指南自动扩展提示词视频处理工具_2101006979501215745.json、图片生成/图生图/MiniMax H3双图参考剧情短片｜有声视频叙事创作利器_2113555231446495233.json、图片生成/图生图/MiniMax H3视频添加物品视频编辑，视频超分风格转换处理工具_2103899733600333826.json、图片生成/图生图/MiniMaxH3视频添加物品编辑｜往已拍视频里塞新东西超简单_2103668392619237378.json…）

- **类型**：Text To Image
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 23 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 22/23 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 21/23 个有
- `VAEDecodeAudio` —— 21/23 个有
- `MiniMaxH3ReferenceToVideo` —— 19/23 个有
- `GetNode` —— 18/23 个有
- `SetNode` —— 18/23 个有
- `孤海注释` —— 16/23 个有
- `VHS_LoadVideo` —— 15/23 个有
- `LoadImage` —— 14/23 个有
- `PrimitiveStringMultiline` —— 14/23 个有
- `PreviewImage` —— 13/23 个有
- `ImageConcanate` —— 12/23 个有
- `LayerUtility: PurgeVRAM V2` —— 12/23 个有
- `PathchSageAttentionKJ` —— 12/23 个有
- `SaveImage` —— 11/23 个有
- `VRAM_Debug` —— 11/23 个有
- `Text` —— 9/23 个有
- `EmptyImage` —— 7/23 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/23 个有
- `ModelAttentionBackend` —— 5/23 个有
- `ImageConcatenateMulti_UTK` —— 4/23 个有
- `LoadAudio` —— 4/23 个有
- `RHHiddenNodes` —— 4/23 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 4/23 个有
- `Fast Groups Bypasser (rgthree)` —— 3/23 个有
- `MiniMaxH3AddGuide` —— 3/23 个有
- `MiniMaxH3AVDecodeT8` —— 2/23 个有
- `BlockSparseAttention` —— 1/23 个有
- `INTConstant` —— 1/23 个有
- `RunningHub Deepcleaner` —— 1/23 个有
- `easy float` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 23 | 100% |
| 高度 | 80 | 80 - 80 | 23 | 100% |
| 采样步数 | 4 | 4 - 4 | 23 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 23 | 100% |
| 采样算法 | er_sde | - | 23 | 100% |
| 调度器 | beta | - | 23 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 23 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/23 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，23 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，23 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，23 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，23 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，23 个样本，一致性 100%
- 调度器 最常用 beta，23 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 高发问题（23/23 个样本）：Steps较低可能导致细节不足

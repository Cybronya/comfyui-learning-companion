---
name: text_to_image_video_lora_sampler_38
type: Text To Image
frequency: 16
level: strong
coverage: 0.731187
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax-H3视频编辑神器｜一键视频换背景人物类特效_2107652623632519170.json, 视频生成/图生视频/MiniMaxH3 ref2va加速八步采样-图生视频工作流_2087367770194403330.json, 视频生成/图生视频/MiniMaxH3 ref2va四步加速V4版｜图生视频_2090101812916482049.json, 视频生成/图生视频/MiniMaxH38高动态加速流｜人物场景类特效图生视频_2092030919111692289.json, 视频生成/图生视频/MiniMaxH3视频换背景编辑｜人物特效+运镜图生视频处理_2108372748677500929.json, 视频生成/图生视频/MiniMaxH3视频换背景，人物类特效视频生视频编辑器_2111274575668531202.json, 视频生成/图生视频/MiniMaxH3视频换背景｜视频编辑动作迁移生成_2095972447886598146.json, 视频生成/图生视频/MiniMaxH3视频背景替换编辑，其它视频处理全能手_2111278750330605570.json, 视频生成/图生视频/MiniMax_H3视频换背景视频编辑工作流，人物类特效视频生视频处理工具_2109456422231699458.json, 视频生成/图生视频/MiniMax_H3视频换背景视频编辑工作流，人物类特效视频生视频处理方案_2109457359675412482.json, 视频生成/图生视频/ref2va四步加速v4｜MiniMaxH3图生视频极速版_2089456017561186306.json, 视频生成/图生视频/ref2va四步加速v4｜MiniMaxH3图生视频极速版_2091266588484923394.json, 视频生成/图生视频/ref2va四步加速v4｜MiniMaxH3图生视频极速直出_2089807243888914434.json, 视频生成/图生视频/ref2va超级加速版｜MiniMaxH3图生视频1.0分辨率极速出片_2093095662807248897.json, 视频生成/图生视频/ref2va超级加速版｜MiniMaxH3支持1.0分辨率图生视频_2093253169697611778.json, 视频生成/文生视频/MiniMaxH3视频编辑｜文生视频换背景轻松搞定_2101170318881677313.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_38

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3视频编辑神器｜一键视频换背景人物类特效_2107652623632519170.json、视频生成/图生视频/MiniMaxH3 ref2va加速八步采样-图生视频工作流_2087367770194403330.json、视频生成/图生视频/MiniMaxH3 ref2va四步加速V4版｜图生视频_2090101812916482049.json、视频生成/图生视频/MiniMaxH38高动态加速流｜人物场景类特效图生视频_2092030919111692289.json、视频生成/图生视频/MiniMaxH3视频换背景编辑｜人物特效+运镜图生视频处理_2108372748677500929.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 15/16 个有
- `孤海注释` —— 11/16 个有
- `KSamplerSelect` —— 10/16 个有
- `VHS_LoadVideo` —— 9/16 个有
- `ImageConcanate` —— 8/16 个有
- `LayerUtility: PurgeVRAM V2` —— 8/16 个有
- `LoadAudio` —— 8/16 个有
- `LoadImage` —— 8/16 个有
- `PathchSageAttentionKJ` —— 8/16 个有
- `PrimitiveStringMultiline` —— 8/16 个有
- `Text Multiline` —— 8/16 个有
- `VRAM_Debug` —— 8/16 个有
- `ModelPatchTorchSettings` —— 7/16 个有
- `PreviewImage` —— 7/16 个有
- `EmptyImage` —— 6/16 个有
- `ImageScale` —— 6/16 个有
- `MiniMaxH3TurboLoRA` —— 6/16 个有
- `MiniMaxH3TurboSampler` —— 6/16 个有
- `PrimitiveInt` —— 6/16 个有
- `easy compare` —— 6/16 个有
- `SaveImage` —— 4/16 个有
- `Label (rgthree)` —— 2/16 个有
- `Fast Groups Bypasser (rgthree)` —— 1/16 个有
- `FloatConstant` —— 1/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/16 个有
- `easy clearCacheAll` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 16 | 100% |
| 高度 | 80 | 80 - 80 | 16 | 100% |
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 16 | 100% |
| 采样算法 | er_sde | - | 16 | 100% |
| 调度器 | beta | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 高发问题（16/16 个样本）：Steps较低可能导致细节不足

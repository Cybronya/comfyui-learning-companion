---
name: unknown_workflow_sampler_unet_vae_8
type: Unknown Workflow
frequency: 24
level: moderate
coverage: 0.863375
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 多图音频参考工作流_2086330601241661442.json, 视频生成/图生视频/MiniMax H3 导演台多图参考生视频_2085966790018031618.json, 视频生成/图生视频/Minimax图生视频（量化加速版)_2084601874262609921.json, 视频生成/图生视频/Minimax多参生视频(量化加速版)_2084619382487085057.json, 视频生成/图生视频/Minimax多参生视频满血768P二倍速版_2084983011841503233.json, 视频生成/图生视频/VividMuse_MiniMax_H3_图生视频_2084274037685051393.json, 视频生成/图生视频/minimax_h3 参考图生视频+sage加速_2084127001375494145.json, 视频生成/图生视频/minimax_h3_r2v完美视频工作流一_2084929898988269569.json, 视频生成/图生视频/minimax_h3_ref2v_3_2092280813852385282.json, 视频生成/图生视频/minimax_h3_ref2v_4_2092280828972855298.json, 视频生成/图生视频/minimax_h3_ref2v_5_2092280840322637826.json, 视频生成/图生视频/minimax_h3_ref2v_6_2092280852507095041.json, 视频生成/图生视频/minimax_h3_全能参考_2084540405961543681.json, 视频生成/图生视频/minimax多参考出视频_2084278095783227394.json, 视频生成/图生视频/video_minimax_h3_r2v-comfyui官方开源工作流_2084152065667981314.json, 视频生成/图生视频/全模态多图片生视频MiniMax H3_2084270450250702850.json, 视频生成/图生视频/加速版-MiniMax H3｜AI Video Studio PR插件VIP专用多图参考生成视频_2089356847248666626.json, 视频生成/图生视频/海螺H3 多参视频（加速节点-加速版）768P_2085282734813044738.json, 视频生成/文生视频/(2倍速！量化加速版)Minimax文生视频V2_2084645452783382530.json, 视频生成/文生视频/(2倍速！量化加速版)Minimax文生视频V3_2086292004803276802.json, 视频生成/文生视频/Minimax H3高质量融合模型10Eros-图生视频BF16加速_2086859043209039874.json, 视频生成/文生视频/Minimax-H3-文生视频-sage+cache双重加速（5秒3.5分钟）_2084572415069351938.json, 视频生成/文生视频/Minimax-H3-文生视频BF16高质量768P-双重加速（T8-cache）_2085387569700888577.json, 视频生成/文生视频/加速版-MiniMax H3｜AI Video Studio PR插件VIP专用图生视频、文生视频_2089147200021553154.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_8

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 多图音频参考工作流_2086330601241661442.json、视频生成/图生视频/MiniMax H3 导演台多图参考生视频_2085966790018031618.json、视频生成/图生视频/Minimax图生视频（量化加速版)_2084601874262609921.json、视频生成/图生视频/Minimax多参生视频(量化加速版)_2084619382487085057.json、视频生成/图生视频/Minimax多参生视频满血768P二倍速版_2084983011841503233.json…）

- **类型**：Unknown Workflow
- **样本数**：24
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 24 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 23/24 个有
- `ComfyMathExpression` —— 22/24 个有
- `PrimitiveFloat` —— 22/24 个有
- `ResolutionSelector` —— 22/24 个有
- `SaveVideo` —— 19/24 个有
- `LoadImage` —— 18/24 个有
- `MiniMaxH3ReferenceToVideo` —— 15/24 个有
- `PrimitiveStringMultiline` —— 15/24 个有
- `PathchSageAttentionKJ` —— 13/24 个有
- `EasyCache` —— 9/24 个有
- `CR Prompt Text` —— 7/24 个有
- `MiniMaxH3ImageToVideo` —— 7/24 个有
- `MiniMaxH3BlockCacheT8` —— 5/24 个有
- `VHS_VideoCombine` —— 5/24 个有
- `GetVideoComponents` —— 4/24 个有
- `ImageScaleToTotalPixels` —— 2/24 个有
- `ImageUpscaleWithModel` —— 2/24 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/24 个有
- `SFH3MultimodalDirector` —— 2/24 个有
- `UpscaleModelLoader` —— 2/24 个有
- `Seed (rgthree)` —— 1/24 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

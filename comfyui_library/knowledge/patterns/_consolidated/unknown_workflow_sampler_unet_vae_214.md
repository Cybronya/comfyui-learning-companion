---
name: unknown_workflow_sampler_unet_vae_214
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.764571
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/动作迁MINIMAX-H3移ENG角色一致性动作迁移图生视频_2087087046383984642.json, 视频生成/图生视频/多参图生视频-开源版MIniMAXH3_2084494818100731905.json, 视频生成/图生视频/多种参考生视频-MiniMax_h3_r2v-视频音频图片参考_2084132425894031361.json, 视频生成/文生视频/MiniMax H3 全模态多参考视频生成器_2090715767955345410.json, 视频生成/文生视频/MiniMax+H3_全能参考视频工作流_2084920348532887554.json, 视频生成/文生视频/多参生视频-MiniMax_h3_r2v-视频音频图片参考-智能提示词_2084694636374872065.json, 视频生成/文生视频/智能提示词-多参生视频-MiniMax_h3_r2v-视频音频图片参考_2084262166823268354.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_214

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/动作迁MINIMAX-H3移ENG角色一致性动作迁移图生视频_2087087046383984642.json、视频生成/图生视频/多参图生视频-开源版MIniMAXH3_2084494818100731905.json、视频生成/图生视频/多种参考生视频-MiniMax_h3_r2v-视频音频图片参考_2084132425894031361.json、视频生成/文生视频/MiniMax H3 全模态多参考视频生成器_2090715767955345410.json、视频生成/文生视频/MiniMax+H3_全能参考视频工作流_2084920348532887554.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 5/7 个有
- `LoadVideo` —— 4/7 个有
- `VHS_LoadVideo` —— 4/7 个有
- `easy anythingIndexSwitch` —— 4/7 个有
- `easy showAnything` —— 4/7 个有
- `AudioCrop` —— 3/7 个有
- `孤海注释` —— 3/7 个有
- `GetVideoComponents` —— 2/7 个有
- `RH_LLMAPI_Pro_Node` —— 2/7 个有
- `AILab_ImageStitch` —— 1/7 个有
- `CM_IntToFloat` —— 1/7 个有
- `JoinStrings` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `PixaromaLabel` —— 1/7 个有
- `RHHiddenNodes` —— 1/7 个有
- `easy int` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

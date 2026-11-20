---
name: unknown_workflow_upscale_latent_upscale_lora_11
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.420687
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/H3最强电影LORA+巅峰双采去油PRO版_2094788799023894529.json, 视频生成/文生视频/H3最强音频驱动对口型二采，吊打SelfLift_2107840856492429314.json, 视频生成/文生视频/H3至尊工作流之言出法随【金鱼佬框架+吃猪侠定制版】_2097127397882683394.json, 视频生成/文生视频/H3虚幻引擎 赛璐璐风格漫画流-双采FL2-736P高清PRO_2100200797417074689.json, 视频生成/文生视频/Jason_二采_H3-多参考生视频-优化版V2_2108131102580895745.json, 视频生成/文生视频/Jason_二采_H3-多参考生视频-优化版_2095126489397288961.json, 视频生成/文生视频/MiniMax H3 8.29_2093713039521566722.json, 视频生成/文生视频/MiniMax H3 二采去油不爆音加速工作流_2096198192596606977.json, 视频生成/文生视频/MiniMax H3 全能视频V3_2095061357325545474.json, 视频生成/文生视频/MiniMax H3 多合一全能生视频极速+二采优化版_2097343290071928833.json, 视频生成/文生视频/MiniMax H3 武戏全能视频V3_2095388978387185666.json, 视频生成/文生视频/MiniMax H3-双采多参考生视频-优化版（解决画面油、一致性、生成慢问题） 用RH最基础的配置_2094800335167639554.json, 视频生成/文生视频/咩咩咩 MiniMax H3-多参考生视频双采_2096479303428038658.json, 视频生成/文生视频/多参考生视频-优化版_2095077768978591746.json, 视频生成/文生视频/工作流lin_2099078938155896833.json, 视频生成/视频生视频/-MiniMax H3-多参考生视频-优化版_2106660994788446209.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_11

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/文生视频/H3最强电影LORA+巅峰双采去油PRO版_2094788799023894529.json、视频生成/文生视频/H3最强音频驱动对口型二采，吊打SelfLift_2107840856492429314.json、视频生成/文生视频/H3至尊工作流之言出法随【金鱼佬框架+吃猪侠定制版】_2097127397882683394.json、视频生成/文生视频/H3虚幻引擎 赛璐璐风格漫画流-双采FL2-736P高清PRO_2100200797417074689.json、视频生成/文生视频/Jason_二采_H3-多参考生视频-优化版V2_2108131102580895745.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：42%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 15/16 个有
- `SplitSigmas` —— 15/16 个有
- `Text` —— 15/16 个有
- `VAEDecodeAudio` —— 15/16 个有
- `VHS_VideoCombine` —— 15/16 个有
- `LoadAudio` —— 14/16 个有
- `PrimitiveFloat` —— 14/16 个有
- `VHS_LoadVideo` —— 14/16 个有
- `easy float` —— 13/16 个有
- `忽略多组孤海` —— 13/16 个有
- `Fast Groups Bypasser (rgthree)` —— 3/16 个有
- `ModelAttentionBackend` —— 3/16 个有
- `Float` —— 2/16 个有
- `H3SigmaRefiner` —— 2/16 个有
- `AudioCrop` —— 1/16 个有
- `CreateVideo` —— 1/16 个有
- `ExtendIntermediateSigmas` —— 1/16 个有
- `Label (rgthree)` —— 1/16 个有
- `MiniMaxChunkFeedForward` —— 1/16 个有
- `MiniMaxH3BlockCacheT8` —— 1/16 个有
- `MiniMaxH3TurboSampler` —— 1/16 个有
- `MiniMaxLowVRAMAttention` —— 1/16 个有
- `PreviewAudio` —— 1/16 个有
- `SaveVideo` —— 1/16 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

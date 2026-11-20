---
name: unknown_workflow_video_sampler_unet_25
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.458625
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, KSamplerSelect, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, SplitSigmas, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/Our_H3_AudioTalking_2Image_1Audio_2103836296480378882.json, 视频生成/文生视频/YZ金鱼-MiniMax H3-多参考生视频-优化版_2092878871120142337.json, 视频生成/文生视频/YZ金鱼-MiniMax H3-多参考生视频-优化版（自用）_2094632571828260866.json, 视频生成/文生视频/【中远景使用】MiniMax H3 双采去油腻_2094069310686846977.json, 视频生成/文生视频/【去油人脸一致】MiniMax H3全能多参考潜空间放大_2094826523541983233.json, 视频生成/文生视频/动漫短剧文戏最佳组合（混合模型+结构lora+二采潜空间放大）_2094308569922498562.json, 视频生成/文生视频/咩咩咩 MiniMax H3-多参考生视频双采_2096479303428038658.json, 视频生成/文生视频/多参考生视频-优化版_2095077768978591746.json, 视频生成/文生视频/官方 全能参考版单采_2104530172652380161.json, 视频生成/文生视频/工作流lin_2099078938155896833.json, 视频生成/文生视频/直播带货知识分享（混合模型+结构lora+二采潜空间放大）_2094570516450471938.json, 视频生成/文生视频/知识分享单人视频生成器_2103751628326260737.json, 视频生成/文生视频/视频生成API_2099703467815292929.json, 视频生成/视频生视频/-MiniMax H3-多参考生视频-优化版_2106660994788446209.json, 视频生成/视频生视频/1027万象AI+Singularity新模型V2（12秒横屏960分辨率）_2096460541328973825.json, 视频生成/视频生视频/1027万象AI+Singularity新模型V2（12秒竖屏960分辨率）_2096477149321580546.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_25

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/文生视频/Our_H3_AudioTalking_2Image_1Audio_2103836296480378882.json、视频生成/文生视频/YZ金鱼-MiniMax H3-多参考生视频-优化版_2092878871120142337.json、视频生成/文生视频/YZ金鱼-MiniMax H3-多参考生视频-优化版（自用）_2094632571828260866.json、视频生成/文生视频/【中远景使用】MiniMax H3 双采去油腻_2094069310686846977.json、视频生成/文生视频/【去油人脸一致】MiniMax H3全能多参考潜空间放大_2094826523541983233.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：46%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXVConcatAVLatent` —— 15/16 个有
- `LTXVSeparateAVLatent` —— 15/16 个有
- `MinimaxH3LatentUpscaler3D` —— 15/16 个有
- `VAEDecodeAudio` —— 15/16 个有
- `LoadAudio` —— 14/16 个有
- `easy float` —— 14/16 个有
- `LoraLoaderModelOnly` —— 13/16 个有
- `PrimitiveFloat` —— 13/16 个有
- `Text` —— 13/16 个有
- `VHS_LoadVideo` —— 10/16 个有
- `忽略多组孤海` —— 10/16 个有
- `Lora Loader Stack (rgthree)` —— 3/16 个有
- `ModelAttentionBackend` —— 3/16 个有
- `Text Multiline` —— 3/16 个有
- `BlockSparseAttention` —— 2/16 个有
- `Fast Groups Bypasser (rgthree)` —— 2/16 个有
- `Float` —— 2/16 个有
- `AudioSeparation` —— 1/16 个有
- `SolAttnMiniMax` —— 1/16 个有
- `SoundFlow_GetLength` —— 1/16 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/16 个有
- `easy cleanGpuUsed` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

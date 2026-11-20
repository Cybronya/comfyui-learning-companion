---
name: unknown_workflow_video_sampler_unet_16
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.441667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/文生图/MiniMax H3 Ref2VA｜6图多参考·角色一致性·Sage加速_2087595496494948354.json, 平台全量/DS视频自用_2118611589472542721.json, 平台全量/H3动作迁移2.0-进阶版-史诗级强化_2102333311677980674.json, 平台全量/H3动作迁移2.0！进阶版，史诗强化！_2101220991618867202.json, 平台全量/H3动作迁移2.0！进阶版，史诗强化！_2101362792946294786.json, 平台全量/H3动作迁移2.0！进阶版，史诗强化！_2102290942047903746.json, 平台全量/MiniMax H3 Pika lora多参考生视频-旧版二采_2119042366190473217.json, 平台全量/Minimax-H3白膜动作设计工作流_2097843659029962754.json, 平台全量/minimaxH3金鱼哥原版_2104194703834042370.json, 平台全量/人物替换+-Minimax-H3_2097286515801026562.json, 平台全量/小林子MniMaxH3二采高清放大版_2116091255510888450.json, 视频生成/图生视频/MiniMax H3-多参考生视频-优化版_2098769440409219073.json, 视频生成/图生视频/MiniMax H3-多参考生视频-高质量hybrid_2095884837700853761.json, 视频生成/图生视频/MiniMax H3多参生视频优化版_支持参考9图3音3视频_2094385613003911169.json, 视频生成/图生视频/MiniMax H3开源-多参考生视频-优化版_2094015909143867394.json, 视频生成/图生视频/MiniMax H3开源-多参考生视频-优化版_2094045987265404929.json, 视频生成/图生视频/MiniMax H3｜让每一帧，都有电影感_2099151915912359938.json, 视频生成/图生视频/MiniMax+H3-二采优化版_2102312716324130817.json, 视频生成/图生视频/MiniMax+H3-多参考生视频-优化版0909_2097580929232498689.json, 视频生成/图生视频/Minimax-H3多参考双采放大生成视频（Singularity）_2096792911970136066.json, 视频生成/图生视频/双倍高清放大MiniMax H3-多参考生视频-字节DMAD加速版_2106606807736209409.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_16

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/文生图/MiniMax H3 Ref2VA｜6图多参考·角色一致性·Sage加速_2087595496494948354.json、平台全量/DS视频自用_2118611589472542721.json、平台全量/H3动作迁移2.0-进阶版-史诗级强化_2102333311677980674.json、平台全量/H3动作迁移2.0！进阶版，史诗强化！_2101220991618867202.json、平台全量/H3动作迁移2.0！进阶版，史诗强化！_2101362792946294786.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：44%

## 共有节点

全部 21 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXVConcatAVLatent` —— 20/21 个有
- `LTXVSeparateAVLatent` —— 20/21 个有
- `MinimaxH3LatentUpscaler3D` —— 20/21 个有
- `SplitSigmas` —— 20/21 个有
- `VAEDecode` —— 20/21 个有
- `VAEDecodeAudio` —— 20/21 个有
- `VHS_LoadVideo` —— 20/21 个有
- `LoadAudio` —— 19/21 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 19/21 个有
- `Text` —— 19/21 个有
- `easy float` —— 19/21 个有
- `忽略多组孤海` —— 17/21 个有
- `LoraLoaderModelOnly` —— 16/21 个有
- `ModelAttentionBackend` —— 6/21 个有
- `Fast Groups Bypasser (rgthree)` —— 3/21 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/21 个有
- `Lora Loader Stack (rgthree)` —— 3/21 个有
- `SaveVideo` —— 3/21 个有
- `SolAttnMiniMax` —— 3/21 个有
- `easy cleanGpuUsed` —— 3/21 个有
- `CreateVideo` —— 2/21 个有
- `MiniMaxH3AVDecodeT8` —— 2/21 个有
- `Text Multiline` —— 2/21 个有
- `easy loraStack` —— 2/21 个有
- `easy loraStackApply` —— 2/21 个有
- `Astra` —— 1/21 个有
- `BlockSparseAttention` —— 1/21 个有
- `GetImageSizeAndCount` —— 1/21 个有
- `ImageFromBatch` —— 1/21 个有
- `Int` —— 1/21 个有
- `LoadVideo` —— 1/21 个有
- `PrimitiveInt` —— 1/21 个有
- `easy showAnything` —— 1/21 个有
- `孤海注释` —— 1/21 个有
- `获取视频信息` —— 1/21 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

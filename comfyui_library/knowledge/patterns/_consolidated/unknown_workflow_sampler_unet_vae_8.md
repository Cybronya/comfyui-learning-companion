---
name: unknown_workflow_sampler_unet_vae_8
type: Unknown Workflow
frequency: 25
level: moderate
coverage: 0.86324
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MINIMAX-H3图生视频工作流_2102372635475791873.json, 视频生成/图生视频/MINIMAX-H3首尾帧视频_2085192239885668354.json, 视频生成/图生视频/Mini max  H3开源啦(加速版）_2085639639234338818.json, 视频生成/图生视频/Mini max  H3开源啦(效果惊艳）_2084172305701367810.json, 视频生成/图生视频/Mini max  H3开源啦(效果惊艳）_2084193937832632322.json, 视频生成/图生视频/MiniMax H3  动画与风格化影像_2084557369203322882.json, 视频生成/图生视频/MiniMax H3 -多图参考生视频_2084163028865609729.json, 视频生成/图生视频/MiniMax H3 3参考图生成跳舞视频_2089373518189383681.json, 视频生成/图生视频/MiniMax H3 8步加速 智能参考娃娃穿搭视频生成_2085536956800397314.json, 视频生成/图生视频/MiniMax H3 FL2VA 首尾帧生视频｜BF16 20步高质量基线版_2090727907718164481.json, 视频生成/图生视频/MiniMax H3 FL2VA-Lightx2v-官方4步加速lora-V0.1-文生视频_2111345897249533954.json, 视频生成/图生视频/MiniMax H3 Ref2VA多图参考生视频-导演级官方提示词标准化模板_2084942982297505793.json, 视频生成/图生视频/MiniMax H3 Start-and-End Frame Video Workflow_2090702379476930562.json, 视频生成/图生视频/MiniMax H3 多图参考+官方提示词模板+提速40%无劣化 真人短剧剧情演绎_2084620840548786177.json, 视频生成/图生视频/MiniMax H3 多图参考+官方提示词模板+提速40%无劣化_2083480380576976897.json, 视频生成/图生视频/MiniMax H3 极速首尾帧图生视频_2087539459008057345.json, 视频生成/图生视频/MiniMax H3_图生视频工作流_2084485598643048450.json, 视频生成/图生视频/MiniMax H3参考生视频6倍加速48GB高配版_2086446949431078914.json, 视频生成/图生视频/MiniMax H3参考生视频6倍加速48GB高配版_2087554038731722753.json, 视频生成/图生视频/MiniMax H3参考生视频6倍加速48GB高配版_2087554175612841985.json, 视频生成/图生视频/MiniMax H3图生视频6倍加速24GB通用版（优化版）_2086460901921742849.json, 视频生成/图生视频/MiniMax H3图生视频6倍加速48GB高配版_2113597089035939841.json, 视频生成/图生视频/MiniMax+H3+首帧图生视频_2113618062388846594.json, 视频生成/图生视频/minimax_H3_r2v 2倍加速_2084977611708657665.json, 视频生成/图生视频/minimax_H3_r2v 4步lora加速_2085423519835447298.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_8

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（视频生成/图生视频/MINIMAX-H3图生视频工作流_2102372635475791873.json、视频生成/图生视频/MINIMAX-H3首尾帧视频_2085192239885668354.json、视频生成/图生视频/Mini max  H3开源啦(加速版）_2085639639234338818.json、视频生成/图生视频/Mini max  H3开源啦(效果惊艳）_2084172305701367810.json、视频生成/图生视频/Mini max  H3开源啦(效果惊艳）_2084193937832632322.json…）

- **类型**：Unknown Workflow
- **样本数**：25
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 25 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 24/25 个有
- `LoadImage` —— 24/25 个有
- `PrimitiveFloat` —— 24/25 个有
- `ResolutionSelector` —— 24/25 个有
- `SaveVideo` —— 24/25 个有
- `PathchSageAttentionKJ` —— 16/25 个有
- `EasyCache` —— 14/25 个有
- `PrimitiveStringMultiline` —— 14/25 个有
- `MiniMaxH3ImageToVideo` —— 13/25 个有
- `MiniMaxH3ReferenceToVideo` —— 12/25 个有
- `LoraLoaderModelOnly` —— 9/25 个有
- `easy showAnything` —— 9/25 个有
- `ImageResizeKJv2` —— 7/25 个有
- `LoadAudio` —— 5/25 个有
- `VHS_VideoCombine` —— 4/25 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/25 个有
- `SolAttnPatch` —— 3/25 个有
- `Int` —— 2/25 个有
- `MiniMaxH3BlockCacheT8` —— 2/25 个有
- `ResizeImagesByLongerEdge` —— 2/25 个有
- `LayerUtility: PurgeVRAM V2` —— 1/25 个有
- `LoraLoaderBypassModelOnly` —— 1/25 个有
- `RHMiniMaxH3PromptOptimizerCompact` —— 1/25 个有
- `RTXVideoSuperResolution` —— 1/25 个有
- `StringFunction|pysssss` —— 1/25 个有
- `Text` —— 1/25 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

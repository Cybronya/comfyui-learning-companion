---
name: unknown_workflow_video_lora_sampler_269
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.838375
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3超长视频流 一次直出2分15秒视频 （135S）_2101639116063600641.json, 视频生成/图生视频/MiniMaxH3参考加速版自用_2092230388805619714.json, 视频生成/图生视频/MiniMaxH3多参MV生成工作流 By 像素幻想Lab_2087128116820013058.json, 视频生成/图生视频/Minimax_H3_强化锁定镜头_音色绑定_2109202394990075906.json, 视频生成/图生视频/无限长视频流_2105728965766897665.json, 视频生成/图生视频/高尚无限长视频流_2098617968786763777.json, 视频生成/文生视频/MiniMax H3最新音乐驱动多图参考MV生成工作流🐘承象_2087393176142303234.json, 视频生成/文生视频/MiniMax H3超长视频流 一次直出2分15秒视频 （135S）_2101639116063600641.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_269

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3超长视频流 一次直出2分15秒视频 （135S）_2101639116063600641.json、视频生成/图生视频/MiniMaxH3参考加速版自用_2092230388805619714.json、视频生成/图生视频/MiniMaxH3多参MV生成工作流 By 像素幻想Lab_2087128116820013058.json、视频生成/图生视频/Minimax_H3_强化锁定镜头_音色绑定_2109202394990075906.json、视频生成/图生视频/无限长视频流_2105728965766897665.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 7/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/8 个有
- `PrimitiveStringMultiline` —— 6/8 个有
- `MiniMaxH3AddGuide` —— 5/8 个有
- `AudioConcat` —— 4/8 个有
- `GetImageRangeFromBatch` —— 4/8 个有
- `ImageBatchMulti` —— 4/8 个有
- `LayerColor: ColorAdapter` —— 4/8 个有
- `LoadAudio` —— 4/8 个有
- `SaveAudio` —— 4/8 个有
- `Label (rgthree)` —— 3/8 个有
- `Audio Duration (mtb)` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `Int` —— 1/8 个有
- `ModelPreviewOverrideKJ` —— 1/8 个有
- `StringMergeNode` —— 1/8 个有
- `VHS_LoadVideo` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

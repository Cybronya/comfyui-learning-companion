---
name: unknown_workflow_sampler_unet_vae_106
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.878857
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, CreateVideo, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Minimax H3 最新最快4步和8步增速工作流_2088074504017899521.json, 视频生成/文生视频/Minimax H3 最新最快4步和8步增速工作流【AI小王子】_2085957972542447617.json, 视频生成/文生视频/MinimaxH3-全能参考生视频-夏_2093873460580802561.json, 视频生成/文生视频/MinimaxH3参考生成视频工作流_2088693526279319553.json, 视频生成/文生视频/MinimaxH3开源版 9-3-3参考生视频_2095459758181535745.json, 视频生成/文生视频/[Minimax H3]9图片+3音频全能参考_2084583737949511681.json, 视频生成/文生视频/minimaxH3文生+参考生视频_2084286286344581121.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_106

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/Minimax H3 最新最快4步和8步增速工作流_2088074504017899521.json、视频生成/文生视频/Minimax H3 最新最快4步和8步增速工作流【AI小王子】_2085957972542447617.json、视频生成/文生视频/MinimaxH3-全能参考生视频-夏_2093873460580802561.json、视频生成/文生视频/MinimaxH3参考生成视频工作流_2088693526279319553.json、视频生成/文生视频/MinimaxH3开源版 9-3-3参考生视频_2095459758181535745.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 6/7 个有
- `BasicScheduler` —— 5/7 个有
- `KSamplerSelect` —— 5/7 个有
- `LoadVideo` —— 5/7 个有
- `GetVideoComponents` —— 4/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/7 个有
- `MiniMaxH3ImageToVideo` —— 3/7 个有
- `PrimitiveStringMultiline` —— 3/7 个有
- `CR Float To Integer` —— 2/7 个有
- `CR Prompt Text` —— 2/7 个有
- `LoraLoaderBypassModelOnly` —— 2/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `MiniMaxH3DualClockSamplerT8` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `TextInput_` —— 1/7 个有
- `VHS_LoadVideo` —— 1/7 个有
- `easy positive` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

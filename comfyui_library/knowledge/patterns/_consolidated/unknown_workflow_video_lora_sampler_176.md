---
name: unknown_workflow_video_lora_sampler_176
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.586455
common_nodes: [BasicGuider, BasicScheduler, GetNode, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyLoader, MiniMaxH3EasyOutput, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, SamplerCustomAdvanced, SetNode, VAEDecode, VAEDecodeAudio, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/MinimaxH3_极简版多合一工作流_2098944049897103361.json, 图片生成/图生图/MinimaxH3_极简版多合一工作流_2099056311664201729.json, 图片生成/图生图/MinimaxH3_极简版多合一工作流_2099681052972380161.json, 图片生成/文生图/自用YZ金鱼-MinimaxH3 极简版多合一工作流_2088536818726817793.json, 数字人/数字人/Minimax H3开源版 极简版多合一工作流_2089716980113821698.json, 视频生成/图生视频/FASHION walk（自用）_2103838105584365570.json, 视频生成/图生视频/Fenglairh-MinimaxH3 极简全功能工作流_2088627150772596737.json, 视频生成/图生视频/Minimax H3开源版 极简版多l图多声音参考工作流_2108771689168457729.json, 视频生成/图生视频/Minimax H3开源版 极简版多l图多声音参考工作流_2108819302899085314.json, 视频生成/图生视频/Minimax H3开源版 极简版多合一工作流_2087847481521565698.json, 视频生成/图生视频/Minimax H3开源版 极简版多合一工作流_2087885554347233281.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_176

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/MinimaxH3_极简版多合一工作流_2098944049897103361.json、图片生成/图生图/MinimaxH3_极简版多合一工作流_2099056311664201729.json、图片生成/图生图/MinimaxH3_极简版多合一工作流_2099681052972380161.json、图片生成/文生图/自用YZ金鱼-MinimaxH3 极简版多合一工作流_2088536818726817793.json、数字人/数字人/Minimax H3开源版 极简版多合一工作流_2089716980113821698.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：59%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `GetNode`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyLoader`
- `MiniMaxH3EasyOutput`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `VAEDecode`
- `VAEDecodeAudio`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadVideo` —— 9/11 个有
- `Text` —— 9/11 个有
- `ImageResizeKJv2` —— 8/11 个有
- `ResolutionSelector` —— 8/11 个有
- `VAEEncode` —— 8/11 个有
- `VAEEncodeAudio` —— 8/11 个有
- `easy cleanGpuUsed` —— 8/11 个有
- `LTXVConcatAVLatent` —— 6/11 个有
- `PT_H3ConcatAVLatent` —— 5/11 个有
- `EmptyImage` —— 3/11 个有
- `LTXVSeparateAVLatent` —— 3/11 个有
- `MinimaxH3LatentUpscaler3D` —— 3/11 个有
- `PreviewImage` —— 3/11 个有
- `SplitSigmas` —— 3/11 个有
- `Float` —— 2/11 个有
- `PrimitiveStringMultiline` —— 2/11 个有
- `MiniMaxChunkFeedForward` —— 1/11 个有
- `MiniMaxH3BlockCacheT8` —— 1/11 个有
- `MiniMaxLowVRAMAttention` —— 1/11 个有
- `ModelAttentionBackend` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_video_lora_sampler_213
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.588545
common_nodes: [BasicGuider, BasicScheduler, GetNode, KSamplerSelect, LoadAudio, LoadImage, LoadVideo, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyLoader, MiniMaxH3EasyOutput, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, SamplerCustomAdvanced, SetNode, Text, VAEDecode, VAEDecodeAudio, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/反推提示词/MinimaxH3 最优二采多合一工作流_2115136815723270145.json, 图片生成/图生图/MinimaxH3_极简版多合一工作流_2098944049897103361.json, 图片生成/图生图/MinimaxH3_极简版多合一工作流_2099056311664201729.json, 图片生成/图生图/MinimaxH3_极简版多合一工作流_2099681052972380161.json, 图片生成/文生图/自用YZ金鱼-MinimaxH3 极简版多合一工作流_2088536818726817793.json, 平台全量/minimax h3口哨舞生成工作流-带雷动版本_2090804983712272385.json, 数字人/数字人/Minimax H3开源版 极简版多合一工作流_2089716980113821698.json, 视频生成/图生视频/FASHION walk（自用）_2103838105584365570.json, 视频生成/图生视频/Fenglairh-MinimaxH3 极简全功能工作流_2088627150772596737.json, 视频生成/图生视频/H3 I2VA 版一工作流_2114594596541001730.json, 视频生成/图生视频/H3 视频生成_2097170910322192385.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_213

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/反推提示词/MinimaxH3 最优二采多合一工作流_2115136815723270145.json、图片生成/图生图/MinimaxH3_极简版多合一工作流_2098944049897103361.json、图片生成/图生图/MinimaxH3_极简版多合一工作流_2099056311664201729.json、图片生成/图生图/MinimaxH3_极简版多合一工作流_2099681052972380161.json、图片生成/文生图/自用YZ金鱼-MinimaxH3 极简版多合一工作流_2088536818726817793.json…）

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
- `LoadVideo`
- `LoraLoaderModelOnly`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyLoader`
- `MiniMaxH3EasyOutput`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `Text`
- `VAEDecode`
- `VAEDecodeAudio`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXVConcatAVLatent` —— 10/11 个有
- `ImageResizeKJv2` —— 7/11 个有
- `ResolutionSelector` —— 7/11 个有
- `VAEEncode` —— 7/11 个有
- `VAEEncodeAudio` —— 7/11 个有
- `easy cleanGpuUsed` —— 7/11 个有
- `LTXVSeparateAVLatent` —— 4/11 个有
- `MinimaxH3LatentUpscaler3D` —— 4/11 个有
- `SplitSigmas` —— 4/11 个有
- `EmptyImage` —— 3/11 个有
- `PreviewImage` —— 3/11 个有
- `MiniMaxChunkFeedForward` —— 2/11 个有
- `MiniMaxLowVRAMAttention` —— 2/11 个有
- `ModelAttentionBackend` —— 2/11 个有
- `MiniMaxH3BlockCacheT8` —— 1/11 个有
- `Notif-PlaySound` —— 1/11 个有
- `PT_H3ConcatAVLatent` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

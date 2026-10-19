---
name: unknown_workflow_video_lora_sampler_185
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8404
common_nodes: [BasicGuider, CLIPLoader, CR Prompt Text, ComfyMathExpression, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/H3打戏自用（T8流大改）_2101622728154505217.json, 视频生成/图生视频/MiniMax H3 视频复刻：视频编辑、视频翻拍、二创与指定角色替换-长视频直出_2105605446362030081.json, 视频生成/图生视频/MiniMax H3-视频复刻-数字人-加速版-参考生视频-长视频直出_2102344546796523522.json, 视频生成/图生视频/MiniMax H3开源 音频驱动数字人图生视频加速版_2092558393386033154.json, 视频生成/图生视频/MiniMax H3开源版 去油版数字人_口播_唱歌_MV加速版_2088208371999657986.json, 视频生成/图生视频/MiniMax H3开源版 去油版数字人_口播_唱歌_MV加速版_2088234673238536194.json, 视频生成/图生视频/MiniMax H3数字人口播-图+音频生成口播视频工作流_2094979350235009025.json, 视频生成/图生视频/MiniMax H3数字人音乐MV加速版V1_2101835373805658113.json, 视频生成/图生视频/MiniMax H3音频驱动数字人-参考生视频-长视频直出【加速版】_2103404335605571585.json, 视频生成/图生视频/MiniMax H3音频驱动数字人-多人对话-一键实现语音+口型同步_2101937972219305986.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_185

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/H3打戏自用（T8流大改）_2101622728154505217.json、视频生成/图生视频/MiniMax H3 视频复刻：视频编辑、视频翻拍、二创与指定角色替换-长视频直出_2105605446362030081.json、视频生成/图生视频/MiniMax H3-视频复刻-数字人-加速版-参考生视频-长视频直出_2102344546796523522.json、视频生成/图生视频/MiniMax H3开源 音频驱动数字人图生视频加速版_2092558393386033154.json、视频生成/图生视频/MiniMax H3开源版 去油版数字人_口播_唱歌_MV加速版_2088208371999657986.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `SolAttnMiniMax` —— 8/10 个有
- `LoadAudio` —— 7/10 个有
- `孤海注释` —— 4/10 个有
- `LoraLoaderModelOnly` —— 2/10 个有
- `VHS_LoadVideo` —— 2/10 个有
- `AudioCrop` —— 1/10 个有
- `ExtendIntermediateSigmas` —— 1/10 个有
- `H3SigmaRefiner` —— 1/10 个有
- `LoadVideo` —— 1/10 个有
- `MiniMaxChunkFeedForward` —— 1/10 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 1/10 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 1/10 个有
- `MiniMaxLowVRAMAttention` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

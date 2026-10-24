---
name: unknown_workflow_sampler_unet_vae_22
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.9161
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CreateVideo, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/minimax h3图生视频_2092555129097641986.json, 视频生成/文生视频/AI视频生成v2_2089671693664083970.json, 视频生成/文生视频/MiniMax H3｜20步质量基准｜参考生视频_2098317985948721153.json, 视频生成/文生视频/MiniMax H3｜20步质量基准｜首尾帧视频_2098317999458570241.json, 视频生成/文生视频/MiniMax H3｜Larry 4步｜参考生视频_2098331637259001857.json, 视频生成/文生视频/MiniMax H3｜Larry 4步｜首尾帧_2098334091904118785.json, 视频生成/文生视频/MiniMax H3｜Larry 8步｜参考生视频_2098334052255363074.json, 视频生成/文生视频/MiniMax H3｜Larry 8步｜首尾帧_2098334066805395458.json, 视频生成/文生视频/MiniMax H3｜LightX2V 4步｜参考生视频_2098326332844363777.json, 视频生成/文生视频/MiniMax H3｜LightX2V 4步｜首尾帧视频_2098317959839174657.json, 视频生成/文生视频/MiniMax H3｜LightX2V 8步｜参考生视频_2098326323948244994.json, 视频生成/文生视频/MiniMax H3｜LightX2V 8步｜首尾帧视频_2098326342881333250.json, 视频生成/文生视频/Minimax H3 AI萌宠视频工作流（宠物带货15秒1080P）_2092564221451132930.json, 视频生成/文生视频/Minimax H3 文生视频写实加速工作流（含提示词模版10秒1080P）_2095431233298853890.json, 视频生成/文生视频/Minimax H3 文生视频工作流（4步加速、支持15秒1080P）_2090647966460768258.json, 视频生成/文生视频/Minimax 多图参考生视频，超级好用！_2089722417114607617.json, 视频生成/文生视频/Minimax+H3+文生视频写实加速工作流（含提示词模版10秒1080P）_2092135642640769026.json, 音频生成/音频生成/AI视频模型转音频模型_2089669249060134913.json, 音频生成/音频生成/MINIMAX视频模型转音频模型_2090695139621695490.json, 音频生成/音频生成/Minimax H3-AI音乐+声音克隆工作流（超长生成、多音频参考）_2090786847566946305.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_22

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/minimax h3图生视频_2092555129097641986.json、视频生成/文生视频/AI视频生成v2_2089671693664083970.json、视频生成/文生视频/MiniMax H3｜20步质量基准｜参考生视频_2098317985948721153.json、视频生成/文生视频/MiniMax H3｜20步质量基准｜首尾帧视频_2098317999458570241.json、视频生成/文生视频/MiniMax H3｜Larry 4步｜参考生视频_2098331637259001857.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 20 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 17/20 个有
- `KSamplerSelect` —— 16/20 个有
- `LoraLoaderModelOnly` —— 12/20 个有
- `MiniMaxH3TurboLoRA` —— 12/20 个有
- `MiniMaxH3AudioConditioningT8` —— 10/20 个有
- `MiniMaxH3Easy` —— 10/20 个有
- `MiniMaxH3EasyModelAdapter` —— 10/20 个有
- `MiniMaxH3EasyOutput` —— 10/20 个有
- `ModelAttentionBackend` —— 10/20 个有
- `SpectrumApplyMiniMaxH3` —— 6/20 个有
- `MiniMaxH3SigmaShift` —— 4/20 个有
- `MiniMaxH3TurboSampler` —— 4/20 个有
- `ExtendIntermediateSigmas` —— 2/20 个有
- `LoadAudio` —— 2/20 个有
- `SaveAudioAdvanced` —— 2/20 个有
- `easy promptList` —— 2/20 个有
- `LoadVideo` —— 1/20 个有
- `PreviewAudio` —— 1/20 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

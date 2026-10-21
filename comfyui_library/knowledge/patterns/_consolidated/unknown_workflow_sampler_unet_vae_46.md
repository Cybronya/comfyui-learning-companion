---
name: unknown_workflow_sampler_unet_vae_46
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.936083
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CreateVideo, KSamplerSelect, MiniMaxH3Easy, MiniMaxH3EasyModelAdapter, MiniMaxH3EasyOutput, ModelAttentionBackend, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3 文生视频工作流（4步加速、支持15秒1080P）_2090647966460768258.json, 视频生成/图生视频/Minimax H3 模仿跳舞工作流（动作迁移、舞蹈模仿、自动生成提示词）_2102956330800734209.json, 视频生成/图生视频/minimax h3图生视频_2092555129097641986.json, 视频生成/文生视频/AI视频生成v2_2089671693664083970.json, 视频生成/文生视频/Minimax H3 AI萌宠视频工作流（宠物带货15秒1080P）_2092564221451132930.json, 视频生成/文生视频/Minimax H3 文生视频写实加速工作流（含提示词模版10秒1080P）_2095431233298853890.json, 视频生成/文生视频/Minimax H3 文生视频工作流（4步加速、支持15秒1080P）_2090647966460768258.json, 视频生成/文生视频/Minimax 多图参考生视频，超级好用！_2089722417114607617.json, 视频生成/文生视频/Minimax+H3+文生视频写实加速工作流（含提示词模版10秒1080P）_2092135642640769026.json, 音频生成/音频生成/AI视频模型转音频模型_2089669249060134913.json, 音频生成/音频生成/MINIMAX视频模型转音频模型_2090695139621695490.json, 音频生成/音频生成/Minimax H3-AI音乐+声音克隆工作流（超长生成、多音频参考）_2090786847566946305.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_46

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/Minimax H3 文生视频工作流（4步加速、支持15秒1080P）_2090647966460768258.json、视频生成/图生视频/Minimax H3 模仿跳舞工作流（动作迁移、舞蹈模仿、自动生成提示词）_2102956330800734209.json、视频生成/图生视频/minimax h3图生视频_2092555129097641986.json、视频生成/文生视频/AI视频生成v2_2089671693664083970.json、视频生成/文生视频/Minimax H3 AI萌宠视频工作流（宠物带货15秒1080P）_2092564221451132930.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `KSamplerSelect`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyModelAdapter`
- `MiniMaxH3EasyOutput`
- `ModelAttentionBackend`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 10/12 个有
- `MiniMaxH3TurboLoRA` —— 10/12 个有
- `LoadImage` —— 8/12 个有
- `SpectrumApplyMiniMaxH3` —— 8/12 个有
- `ExtendIntermediateSigmas` —— 3/12 个有
- `LoadAudio` —— 2/12 个有
- `LoadVideo` —— 2/12 个有
- `SaveAudioAdvanced` —— 2/12 个有
- `easy promptList` —— 2/12 个有
- `PDGeminiAPIKey` —— 1/12 个有
- `PreviewAudio` —— 1/12 个有
- `PreviewTextNode` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

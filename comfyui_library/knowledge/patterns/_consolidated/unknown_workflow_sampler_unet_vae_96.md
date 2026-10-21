---
name: unknown_workflow_sampler_unet_vae_96
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.883125
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CreateVideo, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/15秒段_一采二采_UI格式_魔法少女_2109253533366312961.json, 视频生成/文生视频/MiniMax H3｜20步质量基准｜参考生视频_2098317985948721153.json, 视频生成/文生视频/MiniMax H3｜20步质量基准｜首尾帧视频_2098317999458570241.json, 视频生成/文生视频/Minimax+H3+Multi-parameter+Reference+Raw+Video_2084191041938345986.json, 视频生成/文生视频/Minimax-h3 多模态全能参考版_2093519190757044225.json, 视频生成/文生视频/MinimaxH3参考生成视频工作流_2088693526279319553.json, 视频生成/文生视频/[Minimax H3]9图片+3音频全能参考_2084583737949511681.json, 视频生成/文生视频/minimaxH3文生+参考生视频_2084286286344581121.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_96

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/15秒段_一采二采_UI格式_魔法少女_2109253533366312961.json、视频生成/文生视频/MiniMax H3｜20步质量基准｜参考生视频_2098317985948721153.json、视频生成/文生视频/MiniMax H3｜20步质量基准｜首尾帧视频_2098317999458570241.json、视频生成/文生视频/Minimax+H3+Multi-parameter+Reference+Raw+Video_2084191041938345986.json、视频生成/文生视频/Minimax-h3 多模态全能参考版_2093519190757044225.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VAEDecodeAudio` —— 7/8 个有
- `MiniMaxH3ReferenceToVideo` —— 6/8 个有
- `ComfyMathExpression` —— 5/8 个有
- `PrimitiveFloat` —— 5/8 个有
- `PrimitiveStringMultiline` —— 5/8 个有
- `ResolutionSelector` —— 5/8 个有
- `LoadAudio` —— 3/8 个有
- `LoadVideo` —— 3/8 个有
- `CR Text` —— 2/8 个有
- `MiniMaxH3AudioConditioningT8` —— 2/8 个有
- `VHS_LoadVideo` —— 2/8 个有
- `GetVideoComponents` —— 1/8 个有
- `GoohaiMinimaxH3LatentUpscalerGH` —— 1/8 个有
- `GoohaiMinimaxH3TiledSampler` —— 1/8 个有
- `MiniMaxH3ImageToVideo` —— 1/8 个有
- `SplitSigmas` —— 1/8 个有
- `Text` —— 1/8 个有
- `TextInput_` —— 1/8 个有
- `VHS_LoadVideoFFmpeg` —— 1/8 个有
- `easy positive` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

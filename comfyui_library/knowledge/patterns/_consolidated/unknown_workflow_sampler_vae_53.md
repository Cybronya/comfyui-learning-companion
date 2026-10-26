---
name: unknown_workflow_sampler_vae_53
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.818
common_nodes: [CreateVideo, LoadAudio, LoadImage, RHMiniMaxH3DecodeAV, RHMiniMaxH3DualSigmaSampler, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3Ref2VAAudioReference, RHMiniMaxH3Ref2VAEncode, RHMiniMaxH3Ref2VAImageReference, RHMiniMaxH3Ref2VAModelLoader, RHMiniMaxH3Ref2VATarget, RHMiniMaxH3Ref2VATextEncoderLoader, RHMiniMaxH3Ref2VAVAELoader, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 Ref2VA开源版-多图参考生视频-支持音频输入_2084499175890317313.json, 视频生成/图生视频/MiniMax H3 Ref2VA开源版-多图参考生视频-支持音频输入_2094970680646389762.json, 视频生成/图生视频/MiniMax H3 ref2va(图片+音频)开源版-多图参考生视频_2084117579903356930.json, 视频生成/图生视频/MiniMax+H3+FL2VA开源版-图像+音频参考生视频_2110975898894819330.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_53

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 Ref2VA开源版-多图参考生视频-支持音频输入_2084499175890317313.json、视频生成/图生视频/MiniMax H3 Ref2VA开源版-多图参考生视频-支持音频输入_2094970680646389762.json、视频生成/图生视频/MiniMax H3 ref2va(图片+音频)开源版-多图参考生视频_2084117579903356930.json、视频生成/图生视频/MiniMax+H3+FL2VA开源版-图像+音频参考生视频_2110975898894819330.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `CreateVideo`
- `LoadAudio`
- `LoadImage`
- `RHMiniMaxH3DecodeAV`
- `RHMiniMaxH3DualSigmaSampler`
- `RHMiniMaxH3EmptyAVLatent`
- `RHMiniMaxH3Ref2VAAudioReference`
- `RHMiniMaxH3Ref2VAEncode`
- `RHMiniMaxH3Ref2VAImageReference`
- `RHMiniMaxH3Ref2VAModelLoader`
- `RHMiniMaxH3Ref2VATarget`
- `RHMiniMaxH3Ref2VATextEncoderLoader`
- `RHMiniMaxH3Ref2VAVAELoader`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 2/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `easy anythingIndexSwitch` —— 2/4 个有
- `easy boolean` —— 2/4 个有
- `easy ifElse` —— 2/4 个有
- `easy int` —— 2/4 个有
- `MuyeTextEditOutput` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

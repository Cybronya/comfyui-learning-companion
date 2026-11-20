---
name: unknown_workflow_sampler_vae_42
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.951222
common_nodes: [CreateVideo, RHMiniMaxH3DecodeAV, RHMiniMaxH3DualSigmaSampler, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3Ref2VAEncode, RHMiniMaxH3Ref2VAModelLoader, RHMiniMaxH3Ref2VATarget, RHMiniMaxH3Ref2VATextEncoderLoader, RHMiniMaxH3Ref2VAVAELoader, SaveVideo]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax+H3+Ref2VA开源版-多图参考生视频_2084485787059576834.json, 视频生成/文生视频/MiniMax+H3+Ref2VA开源版-多图参考生视频_2085563519663169538.json, 视频生成/文生视频/MiniMax+H3+Ref2VA开源版（视频+音频）-多图参考生视频_2084191609020829698.json, 视频生成/文生视频/MiniMax+H3+ref2va(图片+音频)开源版-多图参考生视频_2084185747296444417.json, 视频生成/文生视频/biaozhun3_2085258271216201729.json, 视频生成/文生视频/biaozhun_2084917593449783298.json, 视频生成/文生视频/biaozhun_2_2084988119547473922.json, 视频生成/文生视频/h3开源版Minimax H3视频全能多图片参考音频参考视频生成短剧视频生成_2086684981392396290.json, 视频生成/文生视频/mj-minimax-h3工作流_2085655266246356993.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_42

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/MiniMax+H3+Ref2VA开源版-多图参考生视频_2084485787059576834.json、视频生成/文生视频/MiniMax+H3+Ref2VA开源版-多图参考生视频_2085563519663169538.json、视频生成/文生视频/MiniMax+H3+Ref2VA开源版（视频+音频）-多图参考生视频_2084191609020829698.json、视频生成/文生视频/MiniMax+H3+ref2va(图片+音频)开源版-多图参考生视频_2084185747296444417.json、视频生成/文生视频/biaozhun3_2085258271216201729.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 9 个 workflow 都包含：
- `CreateVideo`
- `RHMiniMaxH3DecodeAV`
- `RHMiniMaxH3DualSigmaSampler`
- `RHMiniMaxH3EmptyAVLatent`
- `RHMiniMaxH3Ref2VAEncode`
- `RHMiniMaxH3Ref2VAModelLoader`
- `RHMiniMaxH3Ref2VATarget`
- `RHMiniMaxH3Ref2VATextEncoderLoader`
- `RHMiniMaxH3Ref2VAVAELoader`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 8/9 个有
- `RHMiniMaxH3Ref2VAImageReference` —— 8/9 个有
- `LoadAudio` —— 6/9 个有
- `RHMiniMaxH3Ref2VAAudioReference` —— 6/9 个有
- `LoadVideo` —— 2/9 个有
- `RHMiniMaxH3Ref2VAVideoReference` —— 2/9 个有
- `WujiCleaner` —— 2/9 个有
- `Audio Duration (mtb)` —— 1/9 个有
- `ComfyMathExpression` —— 1/9 个有
- `CustomCombo` —— 1/9 个有
- `MathExpression|pysssss` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

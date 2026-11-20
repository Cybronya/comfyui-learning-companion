---
name: unknown_workflow_sampler_vae_8
type: Unknown Workflow
frequency: 26
level: moderate
coverage: 0.951115
common_nodes: [CreateVideo, RHMiniMaxH3DecodeAV, RHMiniMaxH3DualSigmaSampler, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3Ref2VAEncode, RHMiniMaxH3Ref2VAModelLoader, RHMiniMaxH3Ref2VATarget, RHMiniMaxH3Ref2VATextEncoderLoader, RHMiniMaxH3Ref2VAVAELoader, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/图生视频 -开源海螺minimax-H3_2084084479559290881.json, 视频生成/图生视频/图生视频 -开源海螺minimax-H3_2084119366114832386.json, 视频生成/图生视频/多图参考生视频_2084141825941659649.json, 视频生成/图生视频/最强开源多图参考生视频-MiniMax H3 FL2VA开源版_2084469254153392130.json, 视频生成/图生视频/海螺Hailuo H3全能参考-视频生成（开源版）_2084157382300626945.json, 视频生成/图生视频/海螺MiniMax H3 -多图参考生视频_2084144047043731457.json, 视频生成/图生视频/老孙AI   MiniMax H3 FL2VA开源版-图像 音频参考生视频_2085947928476217346.json, 视频生成/文生视频/A-5 MiniMax-H3 参考生视频 RH版 _ 文字图片音频视频_2085243506225930242.json, 视频生成/文生视频/MiniMax H3 FL2VA开源版-全能参考生视频-多图多音频_2084449187541905410.json, 视频生成/文生视频/MiniMax H3 FL2VA开源版-多图参考生视频-超低积分消耗_2084193397664997378.json, 视频生成/文生视频/MiniMax H3 FL2VA开源版-多图参考生视频_2094357329327251457.json, 视频生成/文生视频/MiniMax H3 FL2VA开源版-多图参考生视频_2095336216827883522.json, 视频生成/文生视频/MiniMax H3 FL2VA开源版-多图参考生视频_2099754651586486273.json, 视频生成/文生视频/MiniMax H3 Ref2VA开源版-多图参考生视频_2084165309996560385.json, 视频生成/文生视频/MiniMax H3 多图参考 开源版_2084461028041121794.json, 视频生成/文生视频/MiniMax H3 多图参考生视频｜角色·产品·场景一致性｜原生音视频_2095451145740316674.json, 视频生成/文生视频/MiniMax H3 开源版 多图参考生视频 高质版_2084534967345963010.json, 视频生成/文生视频/MiniMax H3 开源版 多图参考生视频_2084814126689382402.json, 视频生成/文生视频/MiniMax H3 开源版-多图参考、图生视频_2084218663955156994.json, 视频生成/文生视频/MiniMax+H3+Ref2VA开源版-多图参考生视频_2084176553600180226.json, 视频生成/文生视频/MiniMax+H3+Ref2VA开源版-多图参考生视频_2084485787059576834.json, 视频生成/文生视频/MiniMax+H3+Ref2VA开源版-多图参考生视频_2085563519663169538.json, 视频生成/文生视频/MiniMax+H3+Ref2VA开源版（视频+音频）-多图参考生视频_2084191609020829698.json, 视频生成/文生视频/MiniMax+H3+ref2va(图片+音频)开源版-多图参考生视频_2084185747296444417.json, 视频生成/文生视频/biaozhun3_2085258271216201729.json, 视频生成/文生视频/mj-minimax-h3工作流_2085655266246356993.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_8

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（视频生成/图生视频/图生视频 -开源海螺minimax-H3_2084084479559290881.json、视频生成/图生视频/图生视频 -开源海螺minimax-H3_2084119366114832386.json、视频生成/图生视频/多图参考生视频_2084141825941659649.json、视频生成/图生视频/最强开源多图参考生视频-MiniMax H3 FL2VA开源版_2084469254153392130.json、视频生成/图生视频/海螺Hailuo H3全能参考-视频生成（开源版）_2084157382300626945.json…）

- **类型**：Unknown Workflow
- **样本数**：26
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 26 个 workflow 都包含：
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
- `LoadImage` —— 25/26 个有
- `RHMiniMaxH3Ref2VAImageReference` —— 25/26 个有
- `LoadAudio` —— 6/26 个有
- `RHMiniMaxH3Ref2VAAudioReference` —— 6/26 个有
- `JjkText` —— 4/26 个有
- `LoadVideo` —— 3/26 个有
- `RHMiniMaxH3Ref2VAVideoReference` —— 3/26 个有
- `easy cleanGpuUsed` —— 3/26 个有
- `WujiCleaner` —— 2/26 个有
- `Audio Duration (mtb)` —— 1/26 个有
- `ComfyMathExpression` —— 1/26 个有
- `CustomCombo` —— 1/26 个有
- `MathExpression|pysssss` —— 1/26 个有
- `ResolutionSelector` —— 1/26 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

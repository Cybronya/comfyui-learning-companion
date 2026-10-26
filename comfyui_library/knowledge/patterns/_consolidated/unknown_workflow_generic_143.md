---
name: unknown_workflow_generic_143
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.857167
common_nodes: [LoadImage, easy cleanGpuUsed, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/反推提示词/(自用)N版 Qwen3.5 图像极速反推V1_2035376634013949954.json, 图片生成/反推提示词/Gemma4-图像反推工作流-26B-Q4_2063247807942840322.json, 图片生成/反推提示词/Gemma4图像反推工作流_2042629856315318274.json, 图片生成/反推提示词/Gemma4图像反推工作流（26B Q8高质量）V2_2042038079652892673.json, 图片生成/反推提示词/Qwen3.5 图像反推工作流_2035372598938308610.json, 图片生成/反推提示词/Qwen3.5 强悍的图像反推工作流_2035648568308015105.json, 图片生成/反推提示词/Qwen3.5--图像反推_2035655088227753985.json, 图片生成/反推提示词/gemma4出 jimen用文字_2044599371559342082.json, 图片生成/反推提示词/gemma4直出短剧漫剧分镜脚本_2043148693875990530.json, 图片生成/反推提示词/空白工作流_2043534147645349889.json, 图片生成/反推提示词/（N版）Gemma4图像反推工作流（31B Q8高质量）V1_2042595096012525569.json, 图片生成/图生图/Llama反推图像反推_2042150217411207169.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_143

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/反推提示词/(自用)N版 Qwen3.5 图像极速反推V1_2035376634013949954.json、图片生成/反推提示词/Gemma4-图像反推工作流-26B-Q4_2063247807942840322.json、图片生成/反推提示词/Gemma4图像反推工作流_2042629856315318274.json、图片生成/反推提示词/Gemma4图像反推工作流（26B Q8高质量）V2_2042038079652892673.json、图片生成/反推提示词/Qwen3.5 图像反推工作流_2035372598938308610.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 12 个 workflow 都包含：
- `LoadImage`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 11/12 个有
- `SaveImage` —— 11/12 个有
- `ShellAgentPluginOutputText` —— 11/12 个有
- `SaveText|pysssss` —— 1/12 个有
- `ShowText` —— 1/12 个有
- `easy showAnything` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
